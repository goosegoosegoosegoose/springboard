/** Given a query string, return array of matching shows:
 *     { id, name, summary, episodesUrl }
 */


/** Search Shows
 *    - given a search term, search for tv shows that
 *      match that query.  The function is async show it
 *       will be returning a promise.
 *
 *   - Returns an array of objects. Each object should include
 *     following show information:
 *    {
        id: <show id>,
        name: <show name>,
        summary: <show summary>,
        image: <an image from the show data, or a default imege if no image exists, (image isn't needed until later)>
      }
 */

async function searchShows(query) {
  // TODO: Make an ajax request to the searchShows api.  Remove
  // hard coded data.

// where/when did we set "query" equal the the input value?
// oh is it in the eventhandler
  

  const res = await axios.get(`http://api.tvmaze.com/search/shows`, { params: {
    q: query
  }});

  // let showIdx = Math.floor(Math.random() * res.data.length);
  // return ([
  //   {
  //     id: res.data[showIdx].show.id,
  //     name: res.data[showIdx].show.name,
  //     summary: res.data[showIdx].show.summary,
  //     image: res.data[showIdx].show.image ? res.data[showIdx].show.image.medium : "https://tinyurl.com/tv-missing"
  //   }
  // ]);
  // this wasn't it
  
  let shows = res.data.map(entries => {
    return {
      id: entries.show.id,
      name: entries.show.name,
      summary: entries.show.summary,
      image: entries.show.image ? entries.show.image.medium : "https://tinyurl.com/tv-missing"
    };
  });
  return shows;
};




/** Populate shows list:
 *     - given list of shows, add shows to DOM
 */

function populateShows(shows) {
  const $showsList = $("#shows-list");
  $showsList.empty();

  for (let show of shows) {
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show" data-show-id="${show.id}">
         <div class="card" data-show-id="${show.id}">
           <div class="card-body">
             <h5 class="card-title">${show.name}</h5>
             <p class="card-text">${show.summary}</p>
           </div>
           <img class="card-img-top" src=${show.image}>
         </div>
         <button type="button" class="btn btn-primary epibutton">Episodes</button>
       </div>
      `);

    $showsList.append($item);
  }
}


/** Handle search form submission:
 *    - hide episodes area
 *    - get list of matching shows and show in shows list
 */

$("#search-form").on("submit", async function handleSearch (evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

  $("#episodes-area").hide();

  let shows = await searchShows(query);

  populateShows(shows);  
});


/** Given a show ID, return list of episodes:
 *      { id, name, season, number }
 */

async function getEpisodes(id) {
//   // TODO: get episodes from tvmaze
//   //       you can get this by making GET request to
//   //       http://api.tvmaze.com/shows/SHOW-ID-HERE/episodes

  let res = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`); 

//   // TODO: return array-of-episode-info, as described in docstring above

  let episodes = res.data.map(episode => {
    return {
      id: episode.id,
      name: episode.name,
      season: episode.season,
      number: episode.number,
    }
  });
  return episodes;
};

function populateEpisodes(episodes) {
  const $episodesList = $(`#episodes-list`);
  $episodesList.empty();

  for (episode of episodes) {
    let $list =
      $(`<li>${episode.name}(season ${episode.season}, number ${episode.number})</li>`);
    $episodesList.append($list);
  }
  $("#episodes-area").show();
}

$(`#shows-list`).on(`click`, ".epibutton", async function handleButton(evt){
  let id = $(evt.target).closest("div").data(`show-id`);
  // for .data to be effective, does the target attribute have to have the class data-show-id=??? so .data(`show-id`) returns the ???
  // $(event.target) for jquery, .data needs a string inside it
  // $("#episodes-area").show();
  // apparently you have to do this in the populateEpisodes function instead? Maybe there isn't a difference
 
  
  let episodes = await getEpisodes(id);
  populateEpisodes(episodes);
});

// couldn't get this button to work
// id is undefined
// jesus christ it was all because i had .data("show.id") instead of .data("show-id") a whole hour wasted
