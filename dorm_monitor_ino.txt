#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define DHTPIN 4
#define DHTTYPE DHT11

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED init failed");
    for (;;)
      ;
  }

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  Serial.print(t);
  Serial.print(",");
  Serial.println(h);
  display.clearDisplay();

  display.setCursor(0, 0);
  display.print("T:");
  display.print(t, 1);
  display.print(" C");

  display.setCursor(0, 35);
  display.print("H:");
  display.print(h, 1);
  display.print(" %");

  display.display();
  delay(2000);
}
