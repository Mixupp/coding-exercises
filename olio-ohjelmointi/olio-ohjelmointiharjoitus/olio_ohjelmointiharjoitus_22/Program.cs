using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Olio_ohjelmointiharjoitus_22
{
    public class Program
    {
        static void Main(string[] args)
        {
            // Call the method and print the current date and time
            string currentDateTime = GetCurrentDateTime();
            Console.WriteLine(currentDateTime);

            Console.ReadLine();

            double ballArea = CalculateBallArea(10);
            Console.WriteLine(ballArea);
            Console.ReadLine();

            PrintMultiplicationTable(2);

            List<int> fibonacciSequence = GenerateFibonacciSequence(10); // Lets place the returned list in to a new list variable

            Console.WriteLine("Fibonacci Sequence:");
            foreach (int number in fibonacciSequence) // Lets print out each number from the list using foreach
            {
                Console.Write(number + " ");
            }
            Console.ReadLine();

            int result = CountRandomNumbersWithinRange(10, 0, 100, 0, 50);

            Console.WriteLine($"Numeroita, jotka osuivat asetettuun väliin oli {result} kpl.");
            Console.ReadLine();

            GuessANumberGame(); // Lets run the game. The method has the relevant code.



        }

        // Method to get the current date and time as a string
        static string GetCurrentDateTime()
        {
            // Get the current date and time
            DateTime currentDateTime = DateTime.Now;

            // Format it as a string in the desired format
            string formattedDateTime = currentDateTime.ToString("yyyy-MM-dd HH:mm:ss");

            return formattedDateTime;
        }

        static double CalculateBallArea(double ballRadius)
        {
            double area = Math.PI * Math.Pow(ballRadius, 2); // We will use the Math class for returning the value of pi and calculate the power


            return area;
        }

        static bool DivadableByTwo(int number)
        {
            if (number % 2 == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        static void PrintMultiplicationTable(int number)
        {
            for (int i = 1; i <= 10; i++)
            {
                int result = number * i;
                Console.WriteLine($"{number} * {i} = {result}");
            }
            Console.ReadLine();
        }
        static List<int> GenerateFibonacciSequence(int count)
        {
            List<int> fibonacciSequence = new List<int>(); // Create a new List of integers to store the Fibonacci sequence

            if (count >= 1)
            {
                fibonacciSequence.Add(0); // If at least 1 Fibonacci number is requested, add 0 to the sequence
            }
            if (count >= 2)
            {
                fibonacciSequence.Add(1); // If at least 2 Fibonacci numbers are requested, add 1 to the sequence
            }

            for (int i = 2; i < count; i++)
            {
                int nextFibonacci = fibonacciSequence[i - 1] + fibonacciSequence[i - 2]; // Calculate the next Fibonacci number by summing the last two numbers
                fibonacciSequence.Add(nextFibonacci); // Add the next Fibonacci number to the sequence
            }

            return fibonacciSequence; // Return the generated Fibonacci sequence
        }

        static int CountRandomNumbersWithinRange(int count, int minValue, int maxValue, int rangeMin, int rangeMax)
        {
            Random random = new Random(); // New instance of the Random class
            int countWithinRange = 0; 

            for (int i = 0; i < count; i++) 
            {
                int randomNumber = random.Next(minValue, maxValue + 1); // Create a random number between a range of min to max

                if (randomNumber >= rangeMin && randomNumber <= rangeMax) // if number is between a set range
                {
                    countWithinRange++; // we add it into the count of numbers within range
                }
            }

            return countWithinRange; // In the end we return the count of numbers that fell within range
        }
        static bool GuessANumberGame()
        {
            int winningNumber = 76;

            while (true)
            {
                Console.WriteLine($"Arvaa numero väliltä 1-200!");

                string userInput = Console.ReadLine();
                 
                if (string.IsNullOrWhiteSpace(userInput)) // Lets check if the input string is not empty
                {
                    Console.WriteLine("Et antanut lukua. Yritä uudelleen.");
                    continue; 
                }

                if (int.TryParse(userInput, out int answer)) // Here we make sure that the input is correctly parsed into an integer
                {
                    if (answer > winningNumber)
                    {
                        Console.WriteLine("Arvaamasi luku on suurempi kuin arvottu.");
                    }
                    else if (answer < winningNumber)
                    {
                        Console.WriteLine("Arvaamasi luku on pienempi kuin arvottu.");
                    }
                    else
                    {
                        Console.WriteLine($"Arvasit oikein! Oikea luku oli {winningNumber}!");
                        return false;
                    }
                }
                else
                {
                    Console.WriteLine("Virheellinen syöte. Anna kokonaisluku."); // This is in the case we cant parse. For example entering a char
                }
            }
        }

    }

}
