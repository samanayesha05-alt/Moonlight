const signupForm = document.getElementById("signupForm");

signupForm.addEventListener("submit",async (event)=>{
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    const userData = {
        name : name,
        email : email,
        password : password,
        role : role
    };


    try {
            const response = await fetch('http://127.0.0.1:8000/auth/register',{
            method : 'POST',
            headers : {
                "Content-Type": "application/json"
            },
            body : JSON.stringify(userData)
        });
        const data = await response.json();

        if (response.status==201){
        alert("Registration Successful!🎉, Redirecting to login in...")
        window.location.href = "login.html"
        }

        else if (response.status==409){
            alert (data.detail);
        } 
        else {
            alert("Registration Failed.")
            console.log(data)
        }
    }
    catch (error) {
        console.error("Error:",error)
        alert ("Unable to connect to the server.")
    }
});