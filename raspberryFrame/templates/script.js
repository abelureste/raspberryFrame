const upload = document.querySelector('#upload');
const imgContainer = document.querySelector('#croppieContainer');
const croppedImage = document.querySelector('#croppedImage');
const cropButton = document.querySelector('#btncrop')
const btnRefresh = document.querySelector('#btnRefresh')

var croppieInstance = new Croppie(imgContainer, {
    viewPort: {width: 800, height: 448},
    boundary: {width: 800, height: 448},
    enableResize: false
});

upload.addEventListener('change', function(e) {
    var file = e.target.files[0];
    var reader = new FileReader();
    reader.onload = function (event) {
        croppieInstance.bind({
            url: event.target.result
        });
    }
    reader.readAsDataURL(file);

    imgContainer.style.display = 'block';
    cropButton.style.display = 'block';
});

cropButton.addEventListener('click', function () {
    croppieInstance.result('canvas').then(function (result) {
        croppedImage.src = result;
        croppedImage.style.display = 'block';

        btnRefresh.style.display = 'block';

        imgContainer.style.display = 'none';
        upload.style.display = 'none';
        cropButton.style.display = 'none';
    });
});
