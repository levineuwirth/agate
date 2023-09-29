//  rsa.c

#include "rsa.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define MAX_DIGITS 1000

typedef struct {
    int digits[MAX_DIGITS];
    int length;
} BigNum;

int randomDigit() {
    return rand() % 9 + 1;
}

char* generateRandomDigitString() {
    int length = rand() % 401 + 200;
    char* str = (char*)malloc((length + 1) * sizeof(char));

    str[0] = randomDigit() + '0';
    for (int i = 1; i < length; i++) {
        str[i] = rand() % 10 + '0';
    }

    // Null-terminate the string
    str[length] = '\0';
    return str;
}

bool isZero(const BigNum *num) {
    for (int i = 0; i < num->length; i++) {
        if (num->digits[i] != 0) {
            return false;
        }
    }
    return true;
}

void initBigNum(BigNum *num) {
    memset(num->digits, 0, sizeof(num->digits));
    num->length = 1;
}

void setBigNumFromString(BigNum *num, const char *str) {
    initBigNum(num);
    int len = strlen(str);
    
    for (int i = len - 1; i >= 0; i--) {
        if (str[i] >= '0' && str[i] <= '9') {
            num->digits[num->length++] = str[i] - '0';
        } else {
            fprintf(stderr, "Invalid character in input string: %c\n", str[i]);
            exit(1);
        }
    }
}

void addBigNums(const BigNum *a, const BigNum *b, BigNum *result) {
    initBigNum(result);
    int carry = 0;
    int i;

    for (i = 0; i < a->length || i < b->length || carry > 0; i++) {
        int sum = a->digits[i] + b->digits[i] + carry;
        result->digits[i] = sum % 10;
        carry = sum / 10;
        result->length++;
    }
}

void printBigNum(const BigNum *num) {
    for (int i = num->length - 1; i >= 0; i--) {
        printf("%d", num->digits[i]);
    }
    printf("\n");
}

int main() {
    srand(time(NULL));
    char* randomStr = generateRandomDigitString();
        printf("Random String: %s\n", randomStr);
        BigNum num;
        setBigNumFromString(&num, randomStr);
        printf("Generated BigNum: ");
        printBigNum(&num);

    return 0;
}

