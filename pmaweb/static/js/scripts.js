(() => {
  'use strict'

  const handleDownloadButtons = () => {
    const downloadButtons = document.querySelectorAll('#downloadBtn')
    downloadButtons.forEach(button => {
      button.addEventListener('click', () => {
        const link = button.href.split('/').pop()
        ga('send', 'event', 'Download', link)
        showDownloadModal(button)
      })
    })
  }

  const showDownloadModal = button => {
    const dlLink = document.getElementById('dl-link')
    const pgpContainer = document.getElementById('pgp-container')
    const pgpLink = document.getElementById('pgp-link')
    const sha256Code = document.getElementById('sha256-code')

    const downloadLink = button.getAttribute('href')
    const pgp = button.getAttribute('data-pgp')
    const sha256 = button.getAttribute('data-sha256')

    if (pgp) {
      pgpLink.href = pgp
    } else {
      pgpContainer.classList.add('d-none')
    }

    dlLink.href = downloadLink
    sha256Code.textContent = sha256

    const downloadModal = new bootstrap.Modal(document.getElementById('downloadModal'))
    downloadModal.show()
  }

  const initializeTooltips = () => {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
  }

  const initializeLightbox = () => {
    const lightboxElements = document.querySelectorAll('[data-toggle="lightbox"]')
    lightboxElements.forEach(el => el.addEventListener('click', Lightbox.initialize))
  }

  window.addEventListener('DOMContentLoaded', () => {
    handleDownloadButtons()
    initializeTooltips()
    initializeLightbox()
  })
})()
