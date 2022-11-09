let button = document.querySelector("button#video-link-button");
button.addEventListener("click", () => {
    let link = document.getElementById('video-link').value;
    let video_id = new URL(link).searchParams.get('v');
    window.location.href = '/video/' + video_id;
});

let link = document.getElementById('video-link');
link.addEventListener("keypress", (event) =>{
    if (event.key === "Enter") {
        button.click();
    }
});

let download_link = document.getElementById("download-link");
download_link.addEventListener("click", () => {
    let form = document.getElementById("download-form");
    form.submit()
});
