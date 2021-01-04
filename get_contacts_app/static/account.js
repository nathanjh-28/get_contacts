const editAccountBtn = document.querySelector('#edit-account')
const editForm = document.querySelector('#edit-profile-form')
const accountInfo = document.getElementById('account-info')


editAccountBtn.addEventListener('click', () => {
    editForm.classList.toggle('hidden')
    accountInfo.classList.toggle('hidden')
})