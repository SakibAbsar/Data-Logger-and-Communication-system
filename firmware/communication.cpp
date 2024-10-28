
#include "communication.h"

void Communication::init() {
    Serial.begin(9600);
}

void Communication::sendData(float temperature, float humidity) {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" C, Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");
}
