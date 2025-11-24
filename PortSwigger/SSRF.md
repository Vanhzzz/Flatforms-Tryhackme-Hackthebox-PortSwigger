<h2>LAB1</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/91c00676-bd00-4674-9695-5c581f5da4c1" />
<h2>The website includes items and a feature to check inventory.</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/d650bade-b577-43ee-9994-e7cc998f762c" />
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/53bfea97-6609-4dc2-bc25-d8f0ecb8f4e5" />
<h2>The function to check inventory and retrieve data from an internal system has the potential to cause an SSRF vulnerability.</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/456e2800-fd3a-4f9f-be11-a57f6af434cc" />
<h2>This is a request when we check the inventory, we see sockApi appear on the server side and the server will query it to see the inventory quantity.</h2>
<h2>Let's try to do it with sockApi=http://localhost/</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/5e60da1c-bc9c-4887-b21d-631849633e33" />
<h2>We see that the request we sent is invalid, but must use stock.weliketoshop.net to check inventory -> We conclude that sockApi only accepts whitelist requests</h2>
<h2>
Many applications accept the username@stock... format to further verify user information, so let's check if the application accepts this type of verification.</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/f705d480-4cf8-4524-b1eb-6796a4623e73" />
<h2>We see that this type of verification is not blocked, so we try to ask if there is a way to trick the input and still have the stock.weliketoshop.net part, -> try using # to comment</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/49a9c63c-6bb9-4f12-8a10-2fe5c67499ad" />
<h2>As expected, using # to comment the string behind will result in losing the stock input.... so now we ask the question is there a way to trick the homepage to still receive the @stock.weliketoshop.net suffix but still return localhost -> Try encoding the url # to see if there is any difference
</h2>
<h2>When encrypting once, there will be no difference because when sending a request, the content will be encrypted once, we will encrypt it a second time.</h2>
<img width=700" height="500" alt="image" src="https://github.com/user-attachments/assets/ab512c09-d7d2-471a-8046-5186eb17fa72" />
<h2>We have successfully fooled the website when the input is localhost but the website still receives the whitelisted string</h2>
<h2>Now, let's find a way to delete carlos inside the Admin panel.</h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/a1c5b4f0-5d68-40b4-9665-8d9f8fc0faf1" />
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/60f500c8-8573-4e0b-9d2a-8a39c8e4cab8" />
<h2>LAB2</h2>



