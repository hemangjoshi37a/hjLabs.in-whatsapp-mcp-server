# Build stage
FROM golang:1.24-alpine AS builder

# Install build dependencies
RUN apk add --no-cache gcc musl-dev sqlite-dev

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source code
COPY . .

# Build the application with CGO enabled for SQLite
RUN CGO_ENABLED=1 GOOS=linux go build -o whatsapp-bridge .

# Runtime stage
FROM alpine:latest

# Install runtime dependencies
RUN apk add --no-cache ca-certificates sqlite-libs

WORKDIR /app

# Copy the binary from builder
COPY --from=builder /app/whatsapp-bridge .

# Create store directory
RUN mkdir -p /app/store

# Environment variables
ENV HTTP_PORT=8080
ENV QR_MODE=terminal

# Expose the API port
EXPOSE 8080

# Volume for persistent data
VOLUME ["/app/store"]

# Run the application
CMD ["./whatsapp-bridge"]
