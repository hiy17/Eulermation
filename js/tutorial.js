function toggleDropdown(header) {
  const content = header.nextElementSibling;
  const arrow = header.querySelector(".arrow");
  content.classList.toggle("active");
  arrow.classList.toggle("active");
}
