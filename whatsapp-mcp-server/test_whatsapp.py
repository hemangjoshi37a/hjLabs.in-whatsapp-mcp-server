"""Tests for the WhatsApp MCP server."""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json


class TestReactToMessage:
    """Tests for the react_to_message function."""

    @patch('whatsapp.requests.post')
    def test_react_to_message_success(self, mock_post):
        """Test successful reaction to a message."""
        from whatsapp import react_to_message

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "Reaction sent successfully"
        }
        mock_post.return_value = mock_response

        success, message = react_to_message("msg123", "chat@jid", "👍")

        assert success is True
        assert "sent" in message.lower() or "success" in message.lower()
        mock_post.assert_called_once()

    @patch('whatsapp.requests.post')
    def test_react_to_message_remove_reaction(self, mock_post):
        """Test removing a reaction by passing empty emoji."""
        from whatsapp import react_to_message

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "Reaction removed successfully"
        }
        mock_post.return_value = mock_response

        success, message = react_to_message("msg123", "chat@jid", "")

        assert success is True
        mock_post.assert_called_once()

    @patch('whatsapp.requests.post')
    def test_react_to_message_api_error(self, mock_post):
        """Test handling of API error response."""
        from whatsapp import react_to_message

        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        success, message = react_to_message("msg123", "chat@jid", "👍")

        assert success is False
        assert "error" in message.lower() or "500" in message

    def test_react_to_message_missing_message_id(self):
        """Test validation for missing message ID."""
        from whatsapp import react_to_message

        success, message = react_to_message("", "chat@jid", "👍")

        assert success is False
        assert "message" in message.lower() and "id" in message.lower()

    def test_react_to_message_missing_chat_jid(self):
        """Test validation for missing chat JID."""
        from whatsapp import react_to_message

        success, message = react_to_message("msg123", "", "👍")

        assert success is False
        assert "chat" in message.lower() and "jid" in message.lower()


class TestSendMessage:
    """Tests for the send_message function."""

    @patch('whatsapp.requests.post')
    def test_send_message_success(self, mock_post):
        """Test successful message sending."""
        from whatsapp import send_message

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "Message sent"
        }
        mock_post.return_value = mock_response

        success, message = send_message("1234567890", "Hello!")

        assert success is True
        mock_post.assert_called_once()

    def test_send_message_missing_recipient(self):
        """Test validation for missing recipient."""
        from whatsapp import send_message

        success, message = send_message("", "Hello!")

        assert success is False
        assert "recipient" in message.lower()


class TestDownloadMedia:
    """Tests for the download_media function."""

    @patch('whatsapp.requests.post')
    def test_download_media_success(self, mock_post):
        """Test successful media download."""
        from whatsapp import download_media

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "path": "/tmp/media/image.jpg",
            "message": "Downloaded successfully"
        }
        mock_post.return_value = mock_response

        result = download_media("msg123", "chat@jid")

        assert result == "/tmp/media/image.jpg"
        mock_post.assert_called_once()

    @patch('whatsapp.requests.post')
    def test_download_media_failure(self, mock_post):
        """Test handling of download failure."""
        from whatsapp import download_media

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": False,
            "message": "Media not found"
        }
        mock_post.return_value = mock_response

        result = download_media("msg123", "chat@jid")

        assert result is None
