<h2><b>LAB1</b></h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/9417530e-3d44-49fa-a037-de8f658f601a" />
<h3>Try logging in with name carlos and password a.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/4e6cefa7-110d-41f2-a6b7-03e698a13ac6" />
<h3>View burp suite to see the data sent in JSON format.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/71a960be-a4b8-4f15-a961-fd1b34746ab0" />
<h3>Try sending 2 passwords as array, server side still receives request, so we use brute force attack with all provided passwords.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/128db31e-a1bc-4214-b34b-5937558a5635" />
<h3>We write a script to create a password array and use a repeater to send the password array to the server.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/3e47f31b-627e-469f-ae83-c1fb048c6e2a" />
<h3>We get the result redirected to carlos page.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/0711ef3d-c05d-4b0f-afb0-11038b2f301a" />
<h3>We get the session in the result, change the session on the website and redirect the website to /my-account?id=carlos.</h3>
<img width="700 height="500" alt="image" src="https://github.com/user-attachments/assets/cf6762fa-93ba-4c29-a86d-e694c450c725" />
<h2><b>LAB2</b></h2>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/59707672-f53b-412c-8c87-fbbc84716d5a" />
<h3>Log in to the given account and try entering the 4-digit security code</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/5cd82b4d-621b-4815-aa38-346ce0c6d8c6" />
<h3>After trying twice wrongly, the website immediately redirects to the login page.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/6d830690-88b3-43ec-8062-96e1675e89a4" />
<h3>Burp suite has 3 login requests which are /login: start login, /login: successful login will redirect to /login2 to authenticate with victim email</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/239cdf09-2a84-4d95-a3d1-69e3802c2ba7" />
<h3>From there we can see, we can brute force password attack with macro feature in burp suite with a login string as above</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/e02d24ab-9bb7-4be3-aebc-18d5834ed217" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/9fe19969-34f9-495c-913c-77901de3a3b1" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/b92f8303-9aa2-4dda-95c2-f05507537f92" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/db9121b5-abe5-485b-ade3-f84ca8cdd75b" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/7ac44fb6-118b-4127-88fa-54144315e5d9" />

<h3>Ok so macro created</h3>
<h3>Next we send this request to Intruder</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/19abbb8b-56cd-41ad-b39f-567a74230d81" />
<h3>The number of requests per submission is 1 time, because if 2 times wrong, it will return to the login page.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/33e41393-6d71-4f6d-beea-95919f096c04" />
<h3>Finally, we found carlos' security code.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/f59d1933-4535-430f-918f-4e5a0c1a2117" />
<h3>We take this login session, edit it on the web and go to the /my-account page.</h3>
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/bb40af62-e476-4ab0-9cd5-49b8b05d9db6" />









