// Sederhana: Tambah notifikasi console saat CTA diklik
document.addEventListener("DOMContentLoaded", function() {
    const cta = document.querySelector(".cta");
    if (cta) {
        cta.addEventListener("click", () => {
            console.log("Tombol konsultasi diklik!");
        });
    }
});

  const toggleBtn = document.getElementById('toggle-btn');
  const fullContent = document.getElementById('full-content');

  let isShown = false;

  toggleBtn.addEventListener('click', () => {
    isShown = !isShown;
    if (isShown) {
      fullContent.style.display = 'block';
      setTimeout(() => fullContent.style.opacity = 1, 50);
      toggleBtn.textContent = 'Read less';
    } else {
      fullContent.style.opacity = 0;
      setTimeout(() => fullContent.style.display = 'none', 500);
      toggleBtn.textContent = 'Read more';
    }
  });


// Tambahkan event listener untuk tombol CTA
// dan tampilkan notifikasi di konsol saat diklik
// Pastikan elemen dengan kelas "cta" ada sebelum menambahkan event listener
// Ini akan membantu dalam debugging dan memastikan interaksi pengguna tercatat
// Pastikan untuk menguji kode ini di konsol browser