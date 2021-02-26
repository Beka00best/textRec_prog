window.onload = () => {

  const uploadFile = document.getElementById("button converter-button");
  const uploadBtn = document.getElementById("button converter-button");
  const uploadText = document.getElementById("upload-text");

  uploadBtn.addEventListener("click", function() {
    uploadFile.click();
  });

  uploadFile.addEventListener("change", function() {
    if(uploadFile.value) {
      uploadText.innerText = uploadFile.value;
    } else {
      uploadText.innerText = "Файл не выбран";
    }
  });
}