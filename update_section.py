import os

path = r'c:\Users\user\Documents\GitHub\generasipenerus\index.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = 2048 # Line 2049
end_idx = 2427   # Line 2427

# Verification (imperfect but good enough)
print(f"Start content: {lines[start_idx].strip()}")
print(f"End content: {lines[end_idx-1].strip()}")

new_content = r"""      <!-- Section: Kenapa Program SMI Cocok -->
      <section class="smi-comparison py-5" style="background-color: #007272;">
        <div class="container">
          <!-- Section Header -->
          <div class="row justify-content-center mb-5" data-aos="fade-up">
            <div class="col-lg-10 text-center">
              <h2 class="fw-bold text-warning mb-3" style="text-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                KENAPA PROGRAM SMI INI COCOK UNTUK ANDA..??
              </h2>
              <div class="mx-auto" style="height: 4px; width: 100px; background: #FFD21F; border-radius: 2px;"></div>
            </div>
          </div>

          <!-- Comparison Table Card -->
          <div class="row justify-content-center" data-aos="fade-up" data-aos-delay="200">
            <div class="col-lg-11 col-xl-10">
              <div class="comparison-card shadow-lg overflow-hidden rounded-4 bg-white">
                <div class="table-responsive">
                  <table class="table mb-0 align-middle custom-table">
                    <thead>
                      <tr>
                        <!-- Before Header -->
                        <th class="w-50 text-center py-4 text-white border-0 position-relative" style="background-color: #13392d;">
                          <div class="header-badge mb-2 bg-white text-dark d-inline-block px-3 py-1 rounded-pill fw-bold shadow-sm" style="font-size: 0.8rem;">MASALAH</div>
                          <div class="fs-4 fw-bold">SEBELUM IKUT SMI</div>
                          <span class="d-block mt-1 text-white-50" style="font-size: 0.85rem;">(KONDISI TEKNIS PESERTA)</span>
                        </th>
                        <!-- After Header -->
                        <th class="w-50 text-center py-4 text-dark border-0 position-relative"
                          style="background: linear-gradient(135deg, #FFD21F 0%, #fff176 100%);">
                          <div class="header-badge mb-2 bg-dark text-white d-inline-block px-3 py-1 rounded-pill fw-bold shadow-sm" style="font-size: 0.8rem;">SOLUSI</div>
                          <div class="fs-4 fw-bold">SETELAH IKUT SMI</div>
                          <span class="d-block mt-1 text-dark-50" style="font-size: 0.85rem;">(HASIL TEKNIS & TERUKUR)</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody class="bg-white">

                      <!-- === 1. Digital Marketing === -->
                      <tr class="category-header">
                        <td colspan="2" class="px-4 py-3 bg-light border-bottom border-secondary">
                          <div class="d-flex align-items-center justify-content-center">
                            <span class="badge bg-primary rounded-circle p-2 me-2 shadow-sm fs-6" style="width:35px; height:35px; display:flex; align-items:center; justify-content:center;">1</span>
                            <h5 class="fw-bold m-0 text-primary">Digital Marketing</h5>
                          </div>
                        </td>
                      </tr>

                      <!-- Row 1 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top position-relative">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">1.</span>
                            <span class="text-secondary">Posting asal rajin, tapi <strong class="text-danger bg-danger-soft px-1">tidak tahu tujuan konten</strong></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">1.</span>
                            <span class="fw-medium">Paham <strong class="text-dark">tujuan tiap konten</strong> (branding, edukasi, closing)</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 2 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">2.</span>
                            <span class="text-secondary">Tidak paham <strong class="text-danger bg-danger-soft px-1">funnel</strong> (awareness-consideration-closing)</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">2.</span>
                            <span class="fw-medium">Bisa menyusun <strong class="text-dark">content funnel</strong> yang efektif</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 3 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">3.</span>
                            <span class="text-secondary">Tidak bisa baca <strong class="text-danger bg-danger-soft px-1">insight IG/TikTok/Ads</strong></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">3.</span>
                            <span class="fw-medium">Mengerti <strong class="text-dark">basic ads: target audiens, copy, CTA</strong></span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 4 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">4.</span>
                            <span class="text-secondary">Leads masuk sedikit, <strong class="text-danger bg-danger-soft px-1">tidak tahu kenapa</strong></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">4.</span>
                            <span class="fw-medium">Bisa membaca <strong class="text-dark">data & insight</strong> untuk perbaikan</span>
                          </div>
                        </td>
                      </tr>
                      <tr class="border-bottom">
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">5.</span>
                            <span class="text-secondary">Mengira digital marketing = "viral"</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">5.</span>
                            <span class="fw-medium">Punya <strong class="text-dark">aset digital nyata</strong> (konten, landing, database)</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Quote Footer -->
                      <tr>
                         <td colspan="2" class="p-3 text-center text-white" style="background-color: #0b2e23;">
                            <div class="d-inline-flex align-items-center justify-content-center px-4 py-1 rounded-pill" style="border: 1px solid rgba(255,255,255,0.2);">
                              <i class="fas fa-quote-left text-warning me-2"></i>
                              <span class="fst-italic fw-medium">"Bukan cuma eksis, tapi menghasilkan leads."</span>
                              <i class="fas fa-quote-right text-warning ms-2"></i>
                            </div>
                         </td>
                      </tr>


                      <!-- === 2. Sales & Marketing === -->
                      <tr class="category-header">
                        <td colspan="2" class="px-4 py-3 bg-light border-bottom border-secondary border-top-0">
                          <div class="d-flex align-items-center justify-content-center mt-3">
                            <span class="badge bg-danger rounded-circle p-2 me-2 shadow-sm fs-6" style="width:35px; height:35px; display:flex; align-items:center; justify-content:center;">2</span>
                            <h5 class="fw-bold m-0 text-danger">Sales & Marketing</h5>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 1 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">1.</span>
                            <span class="text-secondary">Jualan pakai <strong class="text-danger bg-danger-soft px-1">harga dan diskon</strong>, bukan value</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">1.</span>
                            <span class="fw-medium">Punya <strong class="text-dark">alur penjualan jelas</strong> (lead → closing → repeat)</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 2 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">2.</span>
                            <span class="text-secondary">Tidak punya <strong class="text-danger bg-danger-soft px-1">script closing</strong></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">2.</span>
                            <span class="fw-medium">Menguasai <strong class="text-dark">script presentasi & closing</strong></span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 3 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">3.</span>
                            <span class="text-secondary">Follow up asal, tidak terstruktur</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">3.</span>
                            <span class="fw-medium">Bisa mengelola database & follow up</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 4 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">4.</span>
                            <span class="text-secondary">Tidak bisa bedakan <strong class="text-danger bg-danger-soft px-1">prospek panas vs dingin</strong></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">4.</span>
                            <span class="fw-medium">Tahu cara <strong class="text-dark">naikkan conversion</strong>, bukan cuma traffic</span>
                          </div>
                        </td>
                      </tr>
                      <tr class="border-bottom">
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">5.</span>
                            <span class="text-secondary">Takut nawarin produk sendiri</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">5.</span>
                            <span class="fw-medium">Berani jualan karena paham value produk</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Quote Footer -->
                      <tr>
                        <td colspan="2" class="p-3 text-center text-white" style="background-color: #0b2e23;">
                          <div class="d-inline-flex align-items-center justify-content-center px-4 py-1 rounded-pill" style="border: 1px solid rgba(255,255,255,0.2);">
                            <i class="fas fa-quote-left text-warning me-2"></i>
                            <span class="fst-italic fw-medium">"Jualan jadi skill, bukan bakat."</span>
                            <i class="fas fa-quote-right text-warning ms-2"></i>
                          </div>
                        </td>
                      </tr>


                      <!-- === 3. Leadership === -->
                      <tr class="category-header">
                        <td colspan="2" class="px-4 py-3 bg-light border-bottom border-secondary border-top-0">
                          <div class="d-flex align-items-center justify-content-center mt-3">
                            <span class="badge bg-dark rounded-circle p-2 me-2 shadow-sm fs-6" style="width:35px; height:35px; display:flex; align-items:center; justify-content:center;">3</span>
                            <h5 class="fw-bold m-0 text-dark">Leadership</h5>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 1 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">1.</span>
                            <span class="text-secondary">Semua dikerjakan sendiri <span class="small text-muted">(one man show)</span></span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">1.</span>
                            <span class="fw-medium">Bisa membagi peran & tanggung jawab</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 2 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">2.</span>
                            <span class="text-secondary">Sulit ambil keputusan, ragu-ragu</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">2.</span>
                            <span class="fw-medium">Berani ambil keputusan berbasis data & tujuan</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 3 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">3.</span>
                            <span class="text-secondary">Komunikasi ke tim tidak jelas</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">3.</span>
                            <span class="fw-medium">Komunikasi lebih tegas dan jelas</span>
                          </div>
                        </td>
                      </tr>
                      <!-- Row 4 -->
                      <tr>
                        <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">4.</span>
                            <span class="text-secondary">Emosi naik turun saat bisnis seret</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">4.</span>
                            <span class="fw-medium">Mental lebih stabil saat bisnis naik-turun</span>
                          </div>
                        </td>
                      </tr>
                      <tr class="border-bottom">
                         <td class="p-4 border-end border-light align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-danger me-3 fs-5">5.</span>
                            <span class="text-secondary">Tidak punya sistem kerja, hanya niat</span>
                          </div>
                        </td>
                        <td class="p-4 bg-success-soft align-top">
                          <div class="d-flex">
                            <span class="fw-bold text-success me-3 fs-5">5.</span>
                            <span class="fw-medium">Mulai membangun <strong class="text-dark">bisnis yang bisa jalan tanpa dia</strong></span>
                          </div>
                        </td>
                      </tr>
                      <!-- Quote Footer -->
                      <tr>
                        <td colspan="2" class="p-3 text-center text-white" style="background-color: #0b2e23;">
                          <div class="d-inline-flex align-items-center justify-content-center px-4 py-1 rounded-pill" style="border: 1px solid rgba(255,255,255,0.2);">
                            <i class="fas fa-quote-left text-warning me-2"></i>
                            <span class="fst-italic fw-medium">"Dari pekerja keras → pemimpin bisnis."</span>
                            <i class="fas fa-quote-right text-warning ms-2"></i>
                          </div>
                        </td>
                      </tr>

                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <style>
            .bg-danger-soft {
              background-color: rgba(220, 53, 69, 0.1);
              border-radius: 4px;
            }
            .bg-success-soft {
              background-color: #f0fff4 !important;
            }
            .custom-table th, .custom-table td {
               width: 50%;
            }
            @media (max-width: 768px) {
               .smi-comparison h2 {
                 font-size: 1.5rem;
               }
               .custom-table th {
                  font-size: 0.9rem;
               }
               .custom-table th .fs-4 {
                  font-size: 1.1rem !important;
               }
               .custom-table td {
                  padding: 1rem !important;
                  display: block; /* Stack on mobile */
                  width: 100% !important;
                  border-right: none !important;
               }
               .custom-table td.border-end {
                  border-bottom: 1px dashed #ddd; /* Separator for stacked */
                  background-color: #fff5f5; /* Light red background for 'Problem' on mobile to distinguish */
               }
               .custom-table .d-flex {
                 align-items: flex-start;
               }
               .custom-table span.fs-5 {
                 font-size: 1rem !important;
                 min-width: 25px; /* Alignment for numbers */
               }
               .header-badge {
                 display: none !important; /* Save space on mobile */
               }
            }
          </style>
        </div>
      </section>
"""

# Splice content
# We replace [start_idx : end_idx]  (inclusive start, exclusive end in Python slice)
# Note: lines[2427] is the line AFTER the section in standard inclusive/exclusive logic if 2427 was the last line to include.
# My view_file showed line 2427 as `</section>`.
# So I want to Replace lines 2049 (index 2048) through 2427 (index 2426).
# Python slice [2048 : 2427] covers indices 2048...2426. Correct.
lines[start_idx:end_idx] = [new_content + '\n']

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully replaced section.")
