#include <cs50.h> // These are the libraries you'd have to import basically for math operations, user input adn to iterate over strings
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void) // Main method
{
    string text = get_string("Text: "); // Ask the user to enter text
// declare necessary variables
    int letters = 0; 
    int words = 1;
    int sentences = 0;
    
    for (int i = 0; i < strlen(text); i++) // Create a for loop from 0 to length of string (entered by user)
    {
        if (isalpha(text[i])) // If the for loop recognizes a letter while iterating through the string
        {
            letters++; // Increments letter variable
        }
        else if (text[i] == ' ') // If the loop recognizes a space
        {
            words++; // Increments the words variable
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!') // If text recognizes a punctuation
        {
            sentences++; // Increments the sentences variable
        }
    }
    float L = (float) letters / (float) words * 100; // Calculates Letters per 100 words
    float S = (float) sentences / (float) words * 100; // Calculates Sentences per 100 words
    int index = round(0.0588 * L - 0.296 * S - 15.8); // Calculates the index

    if (index < 1) // If index is less than 1
    {
        printf("Before Grade 1\n"); // Displays that grade level is less than 1
    }
    else if (index > 16) // If the index is greater than 16
    {
        printf("Grade 16+\n"); // Displays that grade level is 16+  
    }
    else // If the index is not less than 1 and not greater than 16
    {
        printf("Grade %i\n", index); // Displays this m
    }
}
