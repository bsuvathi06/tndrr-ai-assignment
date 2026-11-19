 Loading weights: 100% 338/338 [00:03<00:00, 119.62it/s]=== 16-bit (FP16) ===
Speed: 29.55 tokens/sec | Peak GPU Memory: 7170.2 MB
Loading weights: 100% 338/338 [00:01<00:00, 361.82it/s]=== 4-bit Quantised (NF4) ===
Speed: 14.74 tokens/sec | Peak GPU Memory: 5402.8 MB

--- Prompt 1: Explain KV cache in transformers in two sentences. ---
16-bit: In the context of transformer models, a key-value (KV) cache is used to store intermediate results and activations during training or infere
4-bit : The key-value (KV) cache is a type of memory used by transformers to store frequently accessed data, allowing for faster access and improved

--- Prompt 2: Write a Python function to check if a string is a palindrome. ---
16-bit: Sure, here's an example of a Python function that checks whether a given string is a palindrome:  ```python def is_palindrome(s):     """   
4-bit : The input string can contain any printable ASCII characters, including letters and digits.  **Function Signature:** ```python def is_palindr

--- Prompt 3: What is the capital of Australia and why was it chosen? ---
16-bit: The capital of Australia is Canberra. It was chosen because it was located in the center of the country, away from any major cities that cou
4-bit : The capital of Australia is Canberra. It was chosen because it is located in the center of the country, which makes it easier to establish a

--- Prompt 4: Summarize the difference between TCP and UDP. ---
16-bit: TCP (Transmission Control Protocol) is a connection-oriented protocol that ensures reliable data transmission by establishing a full-duplex 
4-bit : TCP is a connection-oriented protocol that establishes a full-duplex communication channel between two devices, while UDP is a connectionles

--- Prompt 5: Solve: If 3x + 7 = 22, what is x? ---
16-bit: To solve the equation \(3x + 7 = 22\), we will follow these steps:  1. **Isolate the term with the variable**:    We need to get rid of the 
4-bit : To solve the equation \(3x + 7 = 22\) for \(x\), we will follow these steps:  1. **Isolate the variable term**: Start by subtracting 7 from 

--- Prompt 6: List 3 benefits of database indexing. ---
16-bit: Indexing is a technique used in databases to improve query performance by creating an index on the columns that are frequently searched or s
4-bit : Database indexing is a crucial technique used to improve the performance and efficiency of databases by organizing data in a way that makes 

--- Prompt 7: Translate 'Good morning, how are you?' into French. ---
16-bit: The correct translation is: A) Bonjour, comment ça va? B) Bonsoir, comment ça va? C) Au revoir, comment ça va? D) Salut, comment ça va? To d
4-bit : Answer in English. Sure, here it is: "Good morning, how are you?" Answered in French: "Bonjour, comment ça va?" This translates to "Good mor

--- Prompt 8: Explain overfitting to a 10-year-old. ---
16-bit: Imagine you're trying to draw a picture of your favorite animal, but instead of drawing the actual animal, you keep adding more and more det
4-bit : Sure, I can explain that to you! Overfitting is like when you're trying to build a really cool Lego castle with lots of different pieces and

--- Prompt 9: Write a SQL query to find duplicate emails in a Users table. ---
16-bit: Additionally, the query should also return the count of each email that appears more than once.  Table: Users Columns: id (int), name (varch
4-bit : SELECT email, COUNT(*)  FROM users GROUP BY email HAVING COUNT(*) > 1;

--- Prompt 10: Give one pro and one con of microservices. ---
16-bit: Pro: Microservices allow for greater flexibility in development, as each service can be developed independently by different teams or indivi
4-bit : Pro:   - Increased flexibility in deployment due to the ability to run services independently, allowing for faster development cycles. - Imp
