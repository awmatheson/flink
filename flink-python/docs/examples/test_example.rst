.. ################################################################################
     Licensed to the Apache Software Foundation (ASF) under one
     or more contributor license agreements.  See the NOTICE file
     distributed with this work for additional information
     regarding copyright ownership.  The ASF licenses this file
     to you under the Apache License, Version 2.0 (the
     "License"); you may not use this file except in compliance
     with the License.  You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
    limitations under the License.
   ################################################################################

==================
Testing Examples
==================

This page demonstrates how to include testable code examples in documentation.

Simple Example
--------------

Here's a simple example that can be tested:

.. testcode::

   def add_numbers(a, b):
       """Add two numbers together."""
       return a + b

   # Test the function
   result = add_numbers(2, 3)
   print(result)

.. testoutput::

   5

--------------------

Here's a more complex example with multiple test cases:

.. testcode::

   def calculate_area(length, width):
       """Calculate the area of a rectangle."""
       if length <= 0 or width <= 0:
           raise ValueError("Length and width must be positive")
       return length * width

   # Test cases
   print("Area of 3x4 rectangle:", calculate_area(3, 4))
   print("Area of 5x5 square:", calculate_area(5, 5))

.. testoutput::

   Area of 3x4 rectangle: 12
   Area of 5x5 square: 25

----------------------

Here's an example that tests error handling:

.. testcode::

   try:
       result = calculate_area(-1, 5)
   except ValueError as e:
       print("Error caught:", e)

.. testoutput::

   Error caught: Length and width must be positive

-------------------

Here's an example that demonstrates interactive features:

.. testcode::

   # This would be interactive in a real environment
   user_input = "Hello, World!"
   print("User said:", user_input)
   print("Length:", len(user_input))

.. testoutput::

   User said: Hello, World!
   Length: 13

Note: These examples are automatically tested when you run ``make test-doctest``.
