const container = document.querySelector(".container"),
  pwShowHide = document.querySelectorAll(".showHidePw"),
  pwFields = document.querySelectorAll(".password"),
  signUp = document.querySelector(".signup-link"),
  login = document.querySelector(".login-link");

//   js code to show/hide password and change icon
pwShowHide.forEach((eyeIcon) => {
  console.log(eyeIcon);
  eyeIcon.addEventListener("click", () => {
    pwFields.forEach((pwField) => {
      if (pwField.type === "password") {
        pwField.type = "text";

        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye-slash", "uil-eye");
        });
      } else {
        pwField.type = "password";

        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye", "uil-eye-slash");
        });
      }
    });
  });
});

//show profile dropdown in the header
document.addEventListener("DOMContentLoaded", () => {
  const avatarButton = document.getElementById("avatar-menu-button");
  const avatarMenu = document.getElementById("avatar-menu");

  function toggleDropdown() {
    const isExpanded = avatarMenu.classList.contains("hidden");
    avatarMenu.classList.toggle("hidden");
    avatarButton.setAttribute("aria-expanded", isExpanded);
  }

  avatarButton.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent default button action
    event.stopPropagation();
    toggleDropdown();
  });

  // Close the dropdown when clicking outside
  document.addEventListener("click", (event) => {
    if (
      !avatarButton.contains(event.target) &&
      !avatarMenu.contains(event.target)
    ) {
      avatarMenu.classList.add("hidden");
      avatarButton.setAttribute("aria-expanded", "false");
    }
  });

  // Close the dropdown when pressing Escape key
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !avatarMenu.classList.contains("hidden")) {
      avatarMenu.classList.add("hidden");
      avatarButton.setAttribute("aria-expanded", "false");
    }
  });

  console.log("Tailwind CSS Avatar dropdown initialized");
});

// js code to appear signup and login form
signUp.addEventListener("click", () => {
  container.classList.add("active");
});
login.addEventListener("click", () => {
  container.classList.remove("active");
});

// Smooth scroll for CTA button
document.querySelector("button").addEventListener("click", () => {
  document.getElementById("blogs").scrollIntoView({ behavior: "smooth" });
});

// Contact form submission
document.getElementById("contact-form").addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Message sent! Thank you for reaching out.");
});

// Simple toggle for mobile menu
const mobileMenuButton = document.querySelector(
  'button[aria-controls="mobile-menu"]'
);
const mobileMenu = document.getElementById("mobile-menu");

mobileMenuButton.addEventListener("click", () => {
  const expanded =
    mobileMenuButton.getAttribute("aria-expanded") === "true" || false;
  mobileMenuButton.setAttribute("aria-expanded", !expanded);
  mobileMenu.classList.toggle("hidden");

  // Toggle icon
  mobileMenuButton.querySelector("svg:nth-child(1)").classList.toggle("hidden");
  mobileMenuButton.querySelector("svg:nth-child(2)").classList.toggle("hidden");
});
