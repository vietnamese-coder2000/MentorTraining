function remove_i(e, i){
    var del;
    var first_node = e.parentNode.parentNode;
    del = first_node.firstChild;
    for (j = 0; j < i - 1; j++){
        del = first_node.nextSibling;
    }
    first_node.removeChild(del);
}

function edit(e){
    console.log("song_id: " + e.parentNode.getAttribute("song_id"));
}

function more(e){
    var parent = e.parentNode;
    var first = parent.firstChild.nextSibling;
    var second = first.nextSibling.nextSibling;
    console.log("song_id: " + parent.getAttribute("song_id"));
    console.log("title: " + first.innerHTML);
    console.log("artist: " + second.innerHTML);

}