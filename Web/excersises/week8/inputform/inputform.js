const form = document.getElementById("register_form")

form.addEventListener("submit", function(event) {
    event.preventDefault();
    required_fields = document.getElementsByClassName("required_input");

    for (var field of required_fields) {
        if (field.value == "") {
            alert(`"${field.name}" field required`);
            field.focus();
            return;
        }
    }

    const [fullname, age, email, username, password, re_password] = Array.from(required_fields);
    const addresss = document.getElementById("address");
    const male_sex = document.getElementById("male");
    const female_sex = document.getElementById("female");
    const phone = document.getElementById("phone");
    const courses = document.getElementsByName("courses[]");

    // age check
    if (isNaN(age.value)) {
        alert("Age must be a number! Try again.");
        age.focus();
        return;
    }
    if (age.value < 16) {
        alert("You must be at least 16 years old!");
        age.focus();
        return;
    }

    // email check
    const emailPattern = /^\S+@\S+$/;
    if (!emailPattern.test(email.value)) {
        alert("Email invalid! You must input email of type user@domain");
        email.focus();
        return;
    }

    // username check
    if (username.value.length < 6 || username.value.length > 30) {
        alert("Username length must be between 6 and 30 characters! Try again.");
        username.focus();
        return;
    }

    // password check
    if (password.value.length < 6 || password.value.length > 30) {
        alert("Password length must be between 6 and 30 characters! Try again.");
        password.focus();
        return;
    }
    if (re_password.value.length < 6 || re_password.value.length > 30) {
        alert("Password length must be between 6 and 30 characters! Try again.")
        re_password.focus();
        return;
    } else if (password.value != re_password.value) {
        alert("Password not match! Try again");
        re_password.focus();
        return;
    }

    sir = "";
    if (male_sex.checked) {
        sir = "anh";
    } else if (female_sex.checked) {
        sir = "chi";
    }

    courses_registered = [];
    for (var course of courses) {
        if (course.checked) {
            courses_registered.push(course.value);
        }
    }

    alert(`Chuc mung ${sir} ${fullname.value} da dang ky thanh cong cac khoa hoc: ${courses_registered.join(', ')}`);
});
