CC = gcc
CFLAGS = -Wall -O2
TARGET = imx6qdl_sabre_led

all: $(TARGET)

$(TARGET): imx6qdl_sabre_led.c
	$(CC) $(CFLAGS) -o $(TARGET) imx6qdl_sabre_led.c

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

