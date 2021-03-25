console.log("Let's get this party started!");

const input = $(`#input`);
const gifs = $(`#gifs`);

function appendGif(res){
    // let dataLength = res.data.length;
    // if (dataLength){
        // why use an if statement at all
        let numResults = res.data.length;
        if (numResults){
            let gifIndex = Math.floor(Math.random() * numResults);
            let gifDiv = $(`<div>`);
            let gif = $(`<img>`, {
                // src: res.data.data[gifIndex].images.downsized.url
                src: res.data[gifIndex].images.original.url
                // why
            });
            gifDiv.append(gif);
            gifs.append(gifDiv);
        }
    };

$(`#form`).on("submit", async function(evt) {
    evt.preventDefault();
    let searchQuery = input.val();
    input.val(``);
    
    const resp = await axios.get('http://api.giphy.com/v1/gifs/search', { params: {
        q: searchQuery,
        api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
    }});
    appendGif(resp.data);
});

$(`#remove`).on("click", function() {
    $(`#gifs`).empty();
})

// I really need to remember how to do this
// Wasn't my intention to end up copying the answers but it turned out this way