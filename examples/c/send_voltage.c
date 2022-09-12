// file: send_voltage.c
//
// LCM example program.
//
// compile with:
//  $ gcc -o send_message send_message.c -llcm
//
// On a system with pkg-config, you can also use:
//  $ gcc -o send_message send_message.c `pkg-config --cflags --libs lcm`

#include <lcm/lcm.h>
#include <stdio.h>

#include "exlcm_voltages_t.h"

int main(int argc, char **argv)
{
    lcm_t *lcm = lcm_create(NULL);
    if (!lcm)
        return 1;

    exlcm_voltages_t my_data = {
        .timestamp = 0, .voltages = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0},
    };

    exlcm_voltages_t_publish(lcm, "VOLTAGES", &my_data);

    lcm_destroy(lcm);
    return 0;
}
