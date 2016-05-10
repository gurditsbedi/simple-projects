/*
** Implementation of "cows and bulls" logic game. 4-digit-ed game.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int inputTaker(int);
int inputChecker(int);
int bullCowCalculator(int, int);
int numberGenerator();
int numberLength(int);

int main(){
	int number;
	printf("\nThinking for a number....");
	// Generating the number to be guessed
	number = numberGenerator();
	//printf("\n%d", number);
	printf("\nThinking completed.");
	// Starting the game
	inputTaker(number);
	return 0;
}

/*
**	Takes input from the user and sends for further calcualtions
*/
int inputTaker(int numberToBeGuessed){
	int i=1, inputNumber;
	printf("\n\t\t\t\tCow\tBull\n");
	// taking input guess and passing for checking of the input
	while(1){
		printf("\n%d. Enter your Guess: ",i);
		scanf("%d",&inputNumber);
		if(numberLength(inputNumber)==4 && inputChecker(inputNumber)==0){
			i++;
			printf("\t\t\t\t%d",bullCowCalculator(numberToBeGuessed,inputNumber)/10);
			printf("\t%d",bullCowCalculator(numberToBeGuessed,inputNumber)%10);
		}
		if(i>8){
			printf("\n\nBad luck! Better Luck Next time\nThe number was %d",numberToBeGuessed);
			break;
		}
		if(numberToBeGuessed==inputNumber){
			printf("\n\nCongrats you found the number in %d turns",i-1);
			exit(0);
		}
	}
	return 0;
}

/*
**	Checks the input number for a non-zero and non-digit-repeating.
*/
int inputChecker(int n){
	int n1 = n, nd, test,tester, i, j;
	//printf("\nNo.rec=%d",n1);
	for(i=1;i<4;i++){
		test=n1%10;
		nd=n1;
		if(test==0)
			return -1;
		for(j=1;j<=numberLength(n)-i;j++){
			nd/=10;
			tester=nd%10;
			if(test==tester || tester==0)
				return -1;
		}
		n1/=10;
	}
	return 0;
}

/*
** Returns the value of 'bull' and 'cow' for given input and the numberToBeGuessed
*/
int bullCowCalculator(int n, int inputNumber){
	int i, j, cow=0, bull=0, tester, test, nCopy = n, inputNumberCopy=inputNumber;
	// calculates 'bull' number
	for(i=1;i<=4;i++){
		if(n%10==inputNumber%10){
			//printf("\n--Bull=%d",)
			bull++;
		}
		n/=10;
		inputNumber/=10;
	}
	// reassignment the numbers
	n=nCopy;
	inputNumber=inputNumberCopy;
	// calculates 'cow' + 'bull' number
	for(i=1;i<=4;i++){
		tester=n%10;
		test=inputNumber;
		for(j=1;j<=4;j++){
			if(tester==test%10)
				cow++;
			test/=10;
		}
		n/=10;
	}
	// correcting the 'cow' number
	cow=cow-bull;
	//printf("\n--=%d\t%d",cow,bull);
	return cow*10+bull;
}

/*
**	Generates a non-zero and non-digit-repeating number.
*/
int numberGenerator(){
    int num=0, randDigit, i;
    int numbers[9] = {1,2,3,4,5,6,7,8,9};
	time_t t;
	srand((unsigned) time(&t));

	for(i = 0; i < 4; i++){
        randDigit = rand() % (9-i);
        num = num*10 + numbers[randDigit];
        numbers[randDigit] = numbers[8-i];
	}
	return num;
}

/*
** Calculates the number of digits of the input argument
*/
int numberLength(int n){
	int c=0;
	while(n!=0){
		c++; n/=10;
	}
	return c;
}
