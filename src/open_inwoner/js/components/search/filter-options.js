const radioButtons = document.querySelectorAll(
  '.feedback__options .button-radio__input'
)

;[...radioButtons].forEach((radioButton) => {
  radioButton.addEventListener('click', (event) => {
    const feedbackRemarks = document.querySelectorAll('.feedback__remark')
    ;[...feedbackRemarks].forEach((feedbackRemark) =>
      feedbackRemark.classList.add('feedback__remark--show')
    )
  })
})

let timerId = null

const searchForm = document.getElementById('search-form')

const filterButtons = document.querySelectorAll('.filter .checkbox__input')
;[...filterButtons].forEach((checkbox) => {
  checkbox.addEventListener('change', (event) => {
    clearTimeout(timerId)

    // Set a new interval
    timerId = setTimeout(() => {
      searchForm.submit()
    }, 250)
  })
})
