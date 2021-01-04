const addCommentBtn = document.getElementById('add-comment-btn')
const addCommentForm = document.getElementById('add-comment-form')

addCommentBtn.addEventListener('click', () => {
    addCommentForm.classList.toggle('hidden')
})
