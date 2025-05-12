# irc-bootcamp-programming
<p>Halo, saya Muhammad Zidane Manggala Hartono calon anggota IRC IPB divisi Programming. Before I begin, I would like to explain the story behind how I completed my assignment — and I call it 'The Journey'. <strong> First thing first </strong> I started working on my Arduino and ESP32 project with a positive mindset. <strong>I really enjoy learning by combining things or creating something through trial and error </strong> — it makes me proud when I finally achieve the result I want. And it turns out, it wasn’t as difficult as I imagined (of course, it’s still just a practice assignment, haha) — Thank God. That was just the beginning of my journey, it just like the gate of the complex and big castle which i have to open the door (knowledge) one by one.<br> Here it comes the second, Working with Python to access the camera was something completely new to me. <strong> Doing the research took quite some time, but the process itself was the most exciting part </strong>. As I said earlier, this was the part I described as a castle, where I had to open each door one by one — especially the door to face detection, which took a lot of effort and time. I spent two full days doing research, and it felt like I was lost in a corridor inside this castle of knowledge. There were so many sources, so many methods, yet zero clear way out — like walking through a hallway so brightly lit that you can’t see anything because of the overwhelming light. It was hard, but also fun. I willingly pushed through the stress and stayed up late, eyes wide open, determined to find a way forward. <strong>That was the part two.</strong><br>
<strong>Joining IRC is not just a goal for me</strong> — it's something I’ve been truly passionate about. Throughout this journey, I’ve poured my time, energy, and curiosity into learning, experimenting, and solving problems, even when things got confusing or overwhelming. I enjoy exploring new challenges, and I never hesitate to stay up late, pushing myself to understand what I don’t know yet. <strong>Being part of IRC would give me the opportunity to grow even more, to contribute, and to learn from others who share the same spirit of innovation.</strong>

This journey has taught me that learning is not just about results, but about persistence, curiosity, and joy in the process. And with that, I truly hope to be given the opportunity to continue this journey — this time, with IRC. Thank you.
</p>

<h3>Resume bootcamp</h3>
In the bootcamp, we began by learning about the tools used by each team in IRC. For me personally, as someone focusing on programming VTOLs, the basic skills I needed to master were Python and Roboflow. The essential skills for a programmer in IRC also include Python, C++, and Arduino. These are the foundations for anyone working in embedded systems. We were also taught how to deliver presentations about our division's results, so we could explain them clearly to other divisions. In addition, we learned about the toolchains commonly used, as well as how to collaborate effectively using GitHub.

<h3>Explaining Arduino and ESP32</h3>
🧩 Arduino Explaining
<ol>
<li> <strong>#include </strong> <Servo.h>.<br> Purpose: Includes the Servo library, which provides functions to control servo motors. </li>
<li> Servo myservo;.<br> Purpose: Creates a Servo object named myservo that will be used to control the servo motor.</li>
<li> myservo.attach(9);.<br> Purpose: Connects the myservo object to digital pin 9, where your servo motor's signal wire should be connected.</li>
<li> myservo.write(0);.<br> Purpose: Moves the servo motor to 0 degrees.</li>
<li> delay(1000);. <br> Purpose: Waits for 1 second (1000 milliseconds) before the next command.</li>
<li> Repeat the code <strong>but</strong> change the degrees to 90 and then to 180 </li>
</ol> 


<h3>🔁 Summary of Program Flow:</h3>
<ol>

<li>Move servo to 0°, wait 1 second.</li>
<li>Move servo to 90°, wait 1 second.</li>
<li>Move servo to 180°, wait 1 second.</li>
<li>Repeat forever.</li>
</ol>


🧩 ESP32 Explaining
<ol>
<li> pinMode(26, OUTPUT);Purpose: Sets pin 26 as an output pin.<br>Why? This allows you to send signals to pin 26 (turning an LED on or off) rather than receiving signals from it.</li>
<li> void loop().<br>Purpose: This function loops continuously after setup() finishes running.</li>
<li> digitalWrite(26, 1);.<br>Purpose: Sets pin 26 to HIGH (1), which means it sends a 5V signal (often used to turn on an LED or trigger another component).</li>
<li> digitalWrite(26, 0);.<br>Purpose: Sets pin 26 to LOW (0), which means it sends a 0V signal (turning off an LED or deactivating the component).</li>
<li> digitalWrite(26, 0);.<br>Purpose: This is another LOW signal to pin 26. This line might seem redundant, but it still ensures the pin remains at LOW. </li>
<li> delay(1000);.<br>Purpose: Waits for 1000 milliseconds (1 second) before repeating the loop.</li>
</ol>

<h3>🔁 Summary of Program Flow:</h3>
<ol>
<li> Set pin 26 HIGH (5V).</li>
<li> Set pin 26 LOW (0V).</li>
<li> Set pin 26 LOW (0V) again.</li>
<li> Wait 1 second.</li>
<li> Repeat.</li>
</ol>




