const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit",async(event)=>{
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const loginData = new URLSearchParams();

    loginData.append("username",email);
    loginData.append("password",password);

    try {
        const response = await fetch('http://127.0.0.1:8000/auth/login',{
            method : 'POST',
            headers : {
                "Content-Type" : "application/x-www-form-urlencoded"
            },
            body : loginData
        })

        const data = await response.json();

        if (response.status==200) {
            alert("Successfully Logged In");
            window.location.href = "dashboard.html";
        }

        else if (response.status==401){
            alert("Either email or password is wrong");
            console.log(data.detail);
        }
        else {
            alert("Couldn't Loggin In! Please Try Again");
            console.log(data);
            console.log("Status:",response.status);
            console.log("Respnse:",JSON.stringify(loginData));
        }
    } catch (error){
        console.error("Error:",error);
        alert ("Couldn't connect to the server");
    }
});