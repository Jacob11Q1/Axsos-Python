$(document).ready(function(){

    // AJAX submit for comments
    $(document).on("submit", ".comment-form", function(e){
        e.preventDefault();
        let form = $(this);
        $.post(form.attr("action"), form.serialize(), function(data){
            // Instead of full reload, append the new comment
            let commentHtml = `
                <div class="p-2 mb-2 bg-light rounded comment-box d-flex justify-content-between align-items-center">
                    <span><strong>${data.user}:</strong> ${data.comment}</span>
                    <a href="/delete_comment/${data.id}/" class="text-danger ms-2 delete-comment">x</a>
                </div>
            `;
            form.siblings(".comments").append(commentHtml);
            form.find("input[name='comment']").val("");
        });
    });

    // AJAX delete for messages
    $(document).on("click", ".delete-message", function(e){
        e.preventDefault();
        let btn = $(this);
        $.get(btn.attr("href"), function(){
            btn.closest(".message-card").fadeOut(300, function(){ $(this).remove(); });
        });
    });

    // AJAX delete for comments
    $(document).on("click", ".delete-comment", function(e){
        e.preventDefault();
        let btn = $(this);
        $.get(btn.attr("href"), function(){
            btn.closest(".comment-box").fadeOut(200, function(){ $(this).remove(); });
        });
    });

});
