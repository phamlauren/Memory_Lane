var display_tracks = function(tracks){
    $("#tracks").empty()

    if(tracks.length == 0){
        var no_matches = $("<div>")
        $(no_matches).text("No results found.")
        $(no_matches).addClass("col-md-12")
        $("#tracks").append(no_matches)
    }

    else{
      $.each(tracks, function(i, track){
        var title = track["title"]
        var artist = track["artist"]
        var album = track["album"]
        var year_released = track["year_released"]
        var description = track["description"]
        var category = track["category"]
        var media_link = track["media_link"]
        var track_id = track["id"]

        var new_track = $("<div>")
        new_track.addClass("row")
        new_track.attr("id", track_id)
        var image_div = $("<div>")
        $(image_div).addClass("col-md-12")
        var image = $("<img src=" + media_link + ">")
        $(image_div).append(image)
        var stack_one = $("<div>")
        $(stack_one).addClass("col-md-5")
        // var artist_array = Array.from(artist)
        $(stack_one).html("<a href=\"http://127.0.0.1:5000/view/" + track_id +"\">" + title + "</a>" + "</br>" + "Artist: " + artist + "</br>" + album + " (" + year_released + ")")
        var stack_two = $("<div>")
        $(stack_two).addClass("col-md-5")
        $(stack_two).html(category + "</br>" + description + "</br>")

        $(new_track).append(image_div)
        $(new_track).append(stack_one)
        $(new_track).append(stack_two)
        var delete_div = $("<div>")
        var delete_button = $("<button>")
        $(delete_div).addClass("col-md-2")
        $(delete_button).addClass("delete")
        $(delete_button).attr("id", track_id)
        $(delete_button).text("X")
        $(delete_div).append(delete_button)
        $(new_track).append(delete_div)
        $("#tracks").append(new_track)
      })
    }
}

var save_track = function(new_track){
    var data_to_save = {
      "title": new_track["title"], 
      "artist1": new_track["artist1"], 
      "artist2": new_track["artist2"], 
      "artist3": new_track["artist3"], 
      "album": new_track["album"],
      "year_released": new_track["year_released"],
      "description": new_track["description"],
      "category": new_track["category"],
      "media_link": new_track["media_link"]
    }   

    $.ajax({
        type: "POST",
        url: "save_track",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            $("#success_message").remove()
            var new_track_id = result["new_track_id"]
            var success_message = $("<div id=\"success_message\">")
            $(success_message).html("You've successfully created a new track.</br><a href=\"http://127.0.0.1:5000/view/" + new_track_id + "\">Here</a> is a link to view.")
            $(".title").prepend(success_message)
            $("#title").val('')
            $("#title-warning").addClass("hidden")
            $("#title").focus()
            $("#artist1").val('')
            $("#artist1-warning").addClass("hidden")
            $("#artist2").val('')
            $("#artist3").val('')
            $("#album").val('')
            $("#album-warning").addClass("hidden")
            $("#year_released").val('')
            $("#year_released-warning").addClass("hidden")
            $("#year_released-number-warning").addClass("hidden")
            $("#description").val('')
            $("#description-warning").addClass("hidden")
            $("#category").val('')
            $("#category-warning").addClass("hidden")
            $("#media_link").val('')
            $("#media_link-warning").addClass("hidden")
            $("#media_link-invalid-warning").addClass("hidden")

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
            var error_msg = $("<div>")
            $(error_msg).text("Oh no! Creation unsuccessful. ¯\_(ツ)_/¯")
            $(".title").empty()
            $(".title").append(error_msg)
        }
    });
}

var save_description = function(edited_track){
    var data_to_save = {
      "id": edited_track["id"],
      "description": edited_track["description"]
    }   

    $.ajax({
        type: "POST",
        url: "/save_description",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var saved_description = result["description"]
            $("#description_box").empty()
            $("#description_box").html(saved_description)
            $("#description_button").empty()
            $("#description_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"edit_description\">Edit</button>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var save_category = function(edited_track){
    var data_to_save = {
      "id": edited_track["id"],
      "category": edited_track["category"]
    }   

    $.ajax({
        type: "POST",
        url: "/save_category",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var saved_category=result["category"]
            $("#category_box").empty()
            $("#category_box").html(saved_category.toUpperCase())
            $("#category_button").empty()
            $("#category_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"edit_category\" value=\"" + saved_category + "\">Edit</button>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var remove_artist1 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/remove_artist1",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            $("#artist1").empty()
            $("#undo_artist").empty()
            $("#undo_artist").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"recover_artist1\">Restore deleted artist</button>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var recover_artist1 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/recover_artist1",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            location.reload()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var remove_artist2 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/remove_artist2",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            $("#artist2").empty()
            $("#undo_artist").empty()
            $("#undo_artist").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"recover_artist2\">Restore deleted artist</button>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var recover_artist2 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/recover_artist2",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            location.reload()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var remove_artist3 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/remove_artist3",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            $("#artist3").empty()
            $("#undo_artist").empty()
            $("#undo_artist").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"recover_artist3\">Restore deleted artist</button>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var recover_artist3 = function(data){
    var data_to_save = {
      "id": data["track_id"]
    }   

    $.ajax({
        type: "POST",
        url: "/recover_artist3",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            location.reload()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
      if(window.location.href.indexOf("create") > -1){
        $("#home_nav").removeClass("active")
        $("#create_nav").addClass("active")
        $("#title").focus()
      }
      else if(window.location.href == "http://127.0.0.1:5000/search_results/"){
        $("#home_nav").removeClass("active")
        $("#all_nav").addClass("active")

      }
      else if(window.location.href.indexOf("search_results") > -1){
        $("#home_nav").removeClass("active")

      }

      $("#search_input").keyup(function(e){
            if(e.key == "Enter"){
                  var search_string = $("#search_input").val()
                  window.location ="/search_results/" + search_string
            }
      })

      $("#submit").click(function(){
            var search_string = $("#search_input").val()
            window.location = "/search_results/" + search_string
      })

      $("#media_link").keyup(function(e){
            if(e.key == "Enter"){
                $("#title-warning").addClass("hidden")
                $("#artist1-warning").addClass("hidden")
                $("#album-warning").addClass("hidden")
                $("#year_released-warning").addClass("hidden")
                $("#year_released-number-warning").addClass("hidden")
                $("#description-warning").addClass("hidden")
                $("#category-warning").addClass("hidden")
                $("#media_link-warning").addClass("hidden")
                $("#media_link-invalid-warning").addClass("hidden")

                found_warnings = false                
                if($("#title").val().trim().length==0){
                    $("#title-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#artist1").val().trim().length==0){
                    $("#artist1-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#album").val().trim().length==0){
                    $("#album-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#year_released").val().trim().length==0){
                    $("#year_released-warning").removeClass("hidden")
                    found_warnings = true
                }
                if(isNaN($("#year_released").val().trim())){
                    $("#year_released-number-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#description").val().trim().length==0){
                    $("#description-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#category").val().trim().length==0){
                    $("#category-warning").removeClass("hidden")
                    found_warnings = true
                }
                if($("#media_link").val().trim().length==0){
                    $("#media_link-warning").removeClass("hidden")
                    found_warnings = true
                }

                if(found_warnings == false){
                    $.get($("#media_link").val(), function() {
                        var new_track = {
                        "title": $("#title").val(),
                        "artist1": $("#artist1").val(),
                        "artist2": $("#artist2").val(),
                        "artist3": $("#artist3").val(),
                        "album": $("#album").val(),
                        "year_released": $("#year_released").val(),
                        "description": $("#description").val(),
                        "category": $("#category").val(),
                        "media_link": $("#media_link").val()
                        }
                        save_track(new_track)
                        console.log("just triggered save function")
                    })
                    .fail(function() { 
                            $("#media_link-invalid-warning").removeClass("hidden")
                    })
                }
            }
      })

      $("#save_track").click(function(){
            $("#title-warning").addClass("hidden")
            $("#artist1-warning").addClass("hidden")
            $("#album-warning").addClass("hidden")
            $("#year_released-warning").addClass("hidden")
            $("#year_released-number-warning").addClass("hidden")
            $("#description-warning").addClass("hidden")
            $("#category-warning").addClass("hidden")
            $("#media_link-warning").addClass("hidden")
            $("#media_link-invalid-warning").addClass("hidden")

            found_warnings = false
            if($("#title").val().trim().length==0){
                $("#title-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#artist1").val().trim().length==0){
                $("#artist1-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#album").val().trim().length==0){
                $("#album-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#year_released").val().trim().length==0){
                $("#year_released-warning").removeClass("hidden")
                found_warnings = true
            }
            if(isNaN($("#year_released").val().trim())){
                $("#year_released-number-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#description").val().trim().length==0){
                $("#description-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#category").val().trim().length==0){
                $("#category-warning").removeClass("hidden")
                found_warnings = true
            }
            if($("#media_link").val().trim().length==0){
                $("#media_link-warning").removeClass("hidden")
                found_warnings = true
            }

            if(found_warnings == false){
                $.get($("#media_link").val(), function() {
                    var new_track = {
                    "title": $("#title").val(),
                    "artist1": $("#artist1").val(),
                    "artist2": $("#artist2").val(),
                    "artist3": $("#artist3").val(),
                    "album": $("#album").val(),
                    "year_released": $("#year_released").val(),
                    "description": $("#description").val(),
                    "category": $("#category").val(),
                    "media_link": $("#media_link").val()
                    }
                    save_track(new_track)
                })
                .fail(function() { 
                        $("#media_link-invalid-warning").removeClass("hidden")
                })
            }
      })
})

$(document).on("click", "#remove_artist1", function(){
    var data = {"track_id": $("#track_id").html()}
    remove_artist1(data)
})

$(document).on("click", "#recover_artist1", function(){
    var data = {"track_id": $("#track_id").html()}
    recover_artist1(data)
})

$(document).on("click", "#remove_artist2", function(){
    var data = {"track_id": $("#track_id").html()}
    remove_artist2(data)
})

$(document).on("click", "#recover_artist2", function(){
    var data = {"track_id": $("#track_id").html()}
    recover_artist2(data)
})

$(document).on("click", "#remove_artist3", function(){
    var data = {"track_id": $("#track_id").html()}
    remove_artist3(data)
})

$(document).on("click", "#recover_artist3", function(){
    var data = {"track_id": $("#track_id").html()}
    recover_artist3(data)
})

$(document).on("click", "#edit_description", function(){
    var current_text = $("#description_box").html()
    $("#description_box").empty()
    $("#description_box").html("<textarea id=\"description\" placeholder=\"Memory\" value=\"" + current_text + "\">" + current_text + "</textarea>")
    $("#description").focus()
    $("#description_button").empty()
    $("#description_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"save_description\">Save</button><button type=\"submit\" class=\"btn btn-primary\" id=\"discard_description\">Discard</button>")
})

$(document).on("click", "#edit_category", function(){
    var current_text = $("#category_box").attr("value")
    $("#category_box").empty()
    $("#category_box").html("<input type=\"text\" id=\"category\" placeholder=\"Playlist category\" value=\"" + current_text + "\"></input>")
    $("#category").focus()
    $("#category_button").empty()
    $("#category_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"save_category\">Save</button><button type=\"submit\" class=\"btn btn-primary\" id=\"discard_category\">Discard</button>")
})

$(document).on("click", "#discard_description", function(){    
    var replace_text = $("#description").attr("value")
    $("#description_box").empty()
    $("#description_box").html(replace_text)
    $("#description_button").empty()
    $("#description_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"edit_description\">Edit</button>")
})

$(document).on("click", "#save_description", function(){
    var updates_to_save = {
        "id": $("#track_id").html(),
        "description": $("#description").val()
    }
    save_description(updates_to_save)
})

$(document).on("click", "#discard_category", function(){    
    var replace_text = $("#category").attr("value")
    $("#category_box").empty()
    $("#category_box").html(replace_text.toUpperCase())
    $("#category_button").empty()
    $("#category_button").html("<button type=\"submit\" class=\"btn btn-primary\" id=\"edit_category\">Edit</button>")
})


$(document).on("click", "#save_category", function(){
    var updates_to_save = {
        "id": $("#track_id").html(),
        "category": $("#category").val()
    }
    save_category(updates_to_save)

})