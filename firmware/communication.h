
#ifndef COMMUNICATION_H
#define COMMUNICATION_H

class Communication {
public:
    static void init();
    static void sendData(float temperature, float humidity);
};

#endif
