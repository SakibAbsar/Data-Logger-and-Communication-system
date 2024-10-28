
#include "sensor_driver.h"
#include "communication.h"

void setup() {
    Serial.begin(9600);
    SensorDriver::init();
    Communication::init();
}

void loop() {
    float temperature = SensorDriver::readTemperature();
    float humidity = SensorDriver::readHumidity();
    Communication::sendData(temperature, humidity);
    delay(1000);  // Log data every second
}
