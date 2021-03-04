window.onload = () => {

  const uploadFile = document.getElementById("upload-file");
  const uploadBtn = document.getElementById("converter-button");
  const uploadText = document.getElementById("upload-text");

  uploadBtn.addEventListener("click", function() {
    uploadFile.click();
  });

  uploadFile.addEventListener("change", function() {
    if(uploadFile.value) {
      uploadText.innerText = uploadFile.value.replace(/C:\\fakepath\\/, '');
    } else {
      uploadText.innerText = "Файл не выбран";
    }
  });
}