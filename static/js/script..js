let searchInput = document.getElementById("searchInput")
let searchSubmitBtn = document.getElementById("searchSubmitBtn")
let searchForm = document.getElementById("searchForm")

searchSubmitBtn.addEventListener('click', (event)=>{
    event.preventDefault();
    if (! searchInput.checkValidity()) {
        searchInput.reportValidity();
    }else{
        let submitURL = `${location.protocol}//${location.host}/search?searchInput=${searchInput.value}`;
        location.href = submitURL;
    }
})


