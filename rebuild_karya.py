import re
import json

with open('karya_backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract Header & Intro from index.html to match the theme perfectly
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

header_part = index_html[:index_html.find('<main class="relative z-10">')]

# We'll build the new body
new_html = header_part + '''
    <main class="relative z-10 pt-28 pb-20 md:pb-32 min-h-screen">
        <section id="portfolio-gallery" class="relative z-10">
            <div class="container mx-auto px-6 sm:px-12 max-w-6xl">
                <!-- Section Header -->
                <div class="mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-6 reveal-on-scroll">
                    <div>
                        <div class="inline-flex items-center gap-3 mb-4">
                            <span class="w-12 h-[2px] bg-yellow-400"></span>
                            <span class="text-yellow-400 font-mono tracking-[0.2em] text-sm uppercase font-bold">Arsip Lengkap</span>
                        </div>
                        <h2 class="font-serif text-4xl sm:text-5xl md:text-6xl font-bold text-white leading-tight drop-shadow-[4px_4px_0_rgba(0,0,0,1)]">
                            Semua <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500 stroke-text-yellow">Karya</span>
                        </h2>
                    </div>
                    <p class="text-gray-400 max-w-md text-sm md:text-base font-sans leading-relaxed bg-black/40 p-4 border-l-4 border-yellow-400">
                        Koleksi lengkap perjalanan kreatif, eksperimen, dan proyek profesional yang pernah saya bangun.
                    </p>
                </div>

                <!-- JRPG VERTICAL STACK LAYOUT -->
                <div class="flex flex-col gap-24 sm:gap-32 w-full max-w-5xl mx-auto">
'''

# 2. Extract the 6 projects from karya_backup.html
project_blocks = re.findall(r'<div class="relative w-full mx-auto group project-trigger(.*?)</p>\s*</div>\s*</div>', html, re.DOTALL)

for idx, block in enumerate(project_blocks):
    # Extract data attributes
    title = re.search(r'data-title="(.*?)"', block).group(1)
    year = re.search(r'data-year="(.*?)"', block).group(1)
    desc = re.search(r'data-desc="(.*?)"', block).group(1)
    category = re.search(r'data-category="(.*?)"', block).group(1)
    tools_str = re.search(r'data-tools="(.*?)"', block)
    tools = tools_str.group(1) if tools_str else ''
    img = re.search(r'data-img="(.*?)"', block).group(1)
    imgs = re.search(r'data-imgs="(.*?)"', block).group(1)
    
    # Split imgs for background
    imgs_list = [i.strip() for i in imgs.split(',') if i.strip()]
    bg1 = imgs_list[1] if len(imgs_list) > 1 else img
    bg2 = imgs_list[2] if len(imgs_list) > 2 else img
    
    tools_html = ""
    if tools:
        for t in tools.split(','):
            tools_html += f'<span class="px-2 py-1 bg-yellow-400/10 border border-yellow-400/30">{t.strip()}</span>\n                                            '

    card_html = f'''
                    <!-- PROYEK {idx+1} -->
                    <div class="w-full shrink-0 reveal-on-scroll">
                        <div class="relative w-full mx-auto group project-trigger cursor-pointer jrpg-frame p-6 sm:p-12"
                             style="--neon-glow-color: #38156e; background: rgba(56, 21, 110, 0.4);"
                             data-title="{title}"
                             data-year="{year}"
                             data-img="{img}"
                             data-imgs="{imgs}"
                             data-desc="{desc}"
                             data-category="{category}"
                             data-tools="{tools}">
                            
                            <div class="text-center mb-8 px-4">
                                <h3 class="font-serif text-2xl sm:text-4xl text-white font-bold tracking-tight drop-shadow-[2px_4px_0_rgba(0,0,0,1)]">
                                    {title}
                                </h3>
                            </div>

                            <div class="flex flex-col lg:flex-row items-center lg:items-start min-h-[400px] relative">
                                <div class="relative w-full lg:w-[60%] h-[250px] sm:h-[400px] shrink-0 pointer-events-none">
                                    <img src="{bg1}" alt="BG 1" class="absolute right-[5%] top-0 w-[60%] aspect-video object-cover border-[3px] border-[#384159] shadow-[8px_8px_0_rgba(0,0,0,1)] opacity-50 group-hover:opacity-75 transition-opacity duration-500">
                                    <img src="{bg2}" alt="BG 2" class="absolute left-0 bottom-0 w-[60%] aspect-video object-cover border-[3px] border-[#384159] shadow-[8px_8px_0_rgba(0,0,0,1)] opacity-50 group-hover:opacity-75 transition-opacity duration-500">
                                    <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[75%] aspect-video z-20 group-hover:scale-105 transition-transform duration-500 shadow-[15px_15px_0_rgba(0,0,0,1)]">
                                        <img src="{img}" alt="Main" class="w-full h-full object-cover border-[4px] border-yellow-400 group-hover:border-white transition-colors duration-500">
                                    </div>
                                </div>
                                <div class="relative w-full lg:w-[40%] mt-8 lg:mt-0 lg:-ml-12 lg:translate-y-12 z-30 px-6 sm:px-12 lg:px-0">
                                    <div class="bg-[#090212]/95 backdrop-blur-md border border-white/10 shadow-[10px_10px_0_rgba(0,0,0,1)] p-6 sm:p-8 rotate-3 group-hover:rotate-0 transition-transform duration-500 pointer-events-auto">
                                        <p class="text-gray-300 font-sans text-sm sm:text-base leading-relaxed">
                                            {desc}
                                        </p>
                                        <div class="mt-4 flex flex-wrap gap-2 text-xs font-mono text-yellow-400">
                                            {tools_html}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
'''
    new_html += card_html

new_html += '''
                </div>

                <!-- DIRECT NOTION LINK BANNER: "Other things i do" -->
                <div class="mt-16 reveal-on-scroll delay-100">
                    <a href="https://app.notion.com/p/Other-Things-I-Do-a5994d66da9c4033bb4705bb2bc45513" target="_blank" rel="noopener noreferrer" 
                       class="jrpg-frame p-8 sm:p-10 border-4 border-yellow-400 bg-[#38156e]/80 hover:bg-[#38156e] transition-all duration-300 group flex flex-col md:flex-row items-center justify-between gap-6 shadow-[10px_10px_0_rgba(0,0,0,1)] hover:shadow-[15px_15px_0_rgba(0,0,0,1)] hover:-translate-y-1 relative" 
                       style="--neon-glow-color: #ffd460;">
                        
                        <div class="flex items-center gap-5 z-10 w-full md:w-auto">
                            <div class="w-16 h-16 bg-[#090212] border-2 border-yellow-400 flex items-center justify-center text-yellow-400 text-3xl shadow-[4px_4px_0_rgba(0,0,0,1)] group-hover:scale-110 transition-transform shrink-0">
                                <i class="fas fa-bookmark"></i>
                            </div>
                            <div>
                                <span class="text-xs font-mono text-yellow-400 uppercase tracking-widest block mb-1">Notion Workspace</span>
                                <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white group-hover:text-yellow-400 transition-colors drop-shadow-[2px_2px_0_rgba(0,0,0,1)]">Other things i do</h3>
                                <p class="text-sm text-gray-300 font-sans mt-2">Eksplorasi proyek sampingan, catatan riset, dokumentasi studi, dan eksperimen kreatif lainnya di Notion.</p>
                            </div>
                        </div>

                        <div class="z-10 shrink-0 w-full md:w-auto text-right md:text-left mt-4 md:mt-0">
                            <span class="px-6 py-3 font-mono text-xs sm:text-sm tracking-wider uppercase inline-flex items-center justify-center gap-2.5 border-2 border-yellow-400 bg-[#090212] text-yellow-400 font-semibold group-hover:bg-yellow-400 group-hover:text-black transition-all duration-300 shadow-[6px_6px_0_rgba(0,0,0,1)] group-hover:shadow-[4px_4px_0_rgba(0,0,0,1)]">
                                <span>Kunjungi Notion</span>
                                <i class="fas fa-external-link-alt text-xs"></i>
                            </span>
                        </div>
                    </a>
                </div>

            </div>
        </section>
    </main>

    <!-- ===== FOOTER ===== -->
    <footer class="py-8 border-t border-white/5 bg-black/20 backdrop-blur-md relative z-10 text-center text-gray-500 text-xs">
        <p>&copy; Khuluq, Crafted with Antigraviti.</p>
    </footer>

    <!-- ✨ PROJECT DETAIL MODAL WITH 3-IMAGE CAROUSEL & AUTO-SLIDE ✨ -->
    <div id="project-detail-modal" class="fixed inset-0 z-[60] flex items-center justify-center p-4 gemini-modal-overlay">
        <div class="glass-panel w-full max-w-4xl max-h-[92vh] flex flex-col relative overflow-hidden">
            <button id="close-detail-modal-btn" class="absolute top-4 right-4 z-50 w-10 h-10 bg-black/60 hover:bg-black/90 border border-white/20 rounded-full text-white flex items-center justify-center backdrop-blur-md shadow-lg transition-all">
                <i class="fas fa-times"></i>
            </button>
            <div class="flex-grow overflow-y-auto relative z-10 no-scrollbar">
                <!-- Carousel Container -->
                <div id="modal-slider-container" class="w-full h-72 sm:h-[400px] md:h-[450px] relative overflow-hidden group/slider bg-black/40">
                    <div id="modal-slides-track" class="w-full h-full flex transition-transform duration-500 ease-out"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent pointer-events-none z-10"></div>
                    
                    <!-- Prev / Next Navigation Buttons -->
                    <button id="slider-prev-btn" class="absolute left-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 bg-black/60 hover:bg-black/90 border border-white/20 rounded-full text-white flex items-center justify-center backdrop-blur-md shadow-lg transition-all">
                        <i class="fas fa-chevron-left text-sm"></i>
                    </button>
                    <button id="slider-next-btn" class="absolute right-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 bg-black/60 hover:bg-black/90 border border-white/20 rounded-full text-white flex items-center justify-center backdrop-blur-md shadow-lg transition-all">
                        <i class="fas fa-chevron-right text-sm"></i>
                    </button>
                    
                    <!-- Indicator Dots -->
                    <div id="slider-dots" class="absolute bottom-6 left-1/2 -translate-x-1/2 z-20 flex space-x-2"></div>
                </div>

                <!-- Modal Content Details -->
                <div class="p-6 sm:p-10 bg-gradient-to-b from-[#090212] to-[#140728] relative">
                    <div class="flex flex-col md:flex-row justify-between items-start gap-4 mb-6">
                        <div>
                            <span id="detail-modal-year" class="text-orange-400 font-mono text-xs sm:text-sm tracking-widest uppercase mb-2 block"></span>
                            <h3 id="detail-modal-title" class="font-serif text-3xl sm:text-4xl text-white font-bold leading-tight"></h3>
                        </div>
                        <div class="flex gap-3 bg-white/5 border border-white/10 rounded-full px-4 py-2">
                            <span class="text-white/60 text-xs font-mono uppercase tracking-wider">Slide</span>
                            <span id="slider-counter" class="text-orange-400 text-xs font-mono font-bold">1 / 3</span>
                        </div>
                    </div>

                    <p id="detail-modal-desc" class="text-gray-300 text-sm sm:text-base leading-relaxed font-light mb-8 max-w-3xl"></p>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t border-white/10 pt-8">
                        <div>
                            <h4 class="text-white/60 text-xs font-mono uppercase tracking-widest mb-3 flex items-center gap-2">
                                <i class="fas fa-tag text-orange-400"></i> Kategori
                            </h4>
                            <div id="detail-modal-categories" class="flex flex-wrap gap-2"></div>
                        </div>
                        <div>
                            <h4 class="text-white/60 text-xs font-mono uppercase tracking-widest mb-3 flex items-center gap-2">
                                <i class="fas fa-wrench text-orange-400"></i> Tools & Tech
                            </h4>
                            <div id="detail-modal-tools" class="flex flex-wrap gap-2"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ===== JS SCRIPTS ===== -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Langsung memunculkan elemen initial-reveal tanpa preloader
            setTimeout(() => {
                document.querySelectorAll('.initial-reveal').forEach(el => {
                    el.classList.add('entered');
                });
            }, 100);

            // ===== STICKY HEADER SCROLL ENGINE =====
            const headerEl = document.getElementById('header');
            function handleHeaderScroll() {
                if (!headerEl) return;
                if (window.scrollY > 30) {
                    headerEl.classList.add('scrolled');
                } else {
                    headerEl.classList.remove('scrolled');
                }
            }
            window.addEventListener('scroll', handleHeaderScroll, { passive: true });
            handleHeaderScroll();

            // ===== FUTURISTIC SCROLL REVEAL INTERSECTION OBSERVER =====
            const revealElements = document.querySelectorAll('.reveal-on-scroll');
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                    }
                });
            }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

            revealElements.forEach(el => revealObserver.observe(el));

            // 3-IMAGE CAROUSEL & AUTO-SLIDE MODAL LOGIC
            let currentSlide = 0;
            let slideImages = [];
            let autoSlideInterval = null;

            function updateSlider() {
                const track = document.getElementById('modal-slides-track');
                if (!track) return;
                track.style.transform = `translateX(-${currentSlide * 100}%)`;

                const counter = document.getElementById('slider-counter');
                if (counter) counter.textContent = `${currentSlide + 1} / ${slideImages.length}`;

                document.querySelectorAll('.slider-dot').forEach((dot, idx) => {
                    if (idx === currentSlide) {
                        dot.classList.add('bg-white', 'w-6');
                        dot.classList.remove('bg-white/40', 'w-2');
                    } else {
                        dot.classList.remove('bg-white', 'w-6');
                        dot.classList.add('bg-white/40', 'w-2');
                    }
                });
            }

            function startAutoSlide() {
                stopAutoSlide();
                if (slideImages.length > 1) {
                    autoSlideInterval = setInterval(() => {
                        currentSlide = (currentSlide + 1) % slideImages.length;
                        updateSlider();
                    }, 3500); // Auto slide every 3.5 seconds
                }
            }

            function stopAutoSlide() {
                if (autoSlideInterval) {
                    clearInterval(autoSlideInterval);
                    autoSlideInterval = null;
                }
            }

            const modal = document.getElementById('project-detail-modal');
            
            // EVENT DELEGATION UNTUK MEMASTIKAN KLIK SELALU TERTANGKAP
            document.body.addEventListener('click', (e) => {
                const card = e.target.closest('.project-trigger');
                if (!card) return;

                console.log("PROJECT CARD CLICKED!", card);

                const title = card.getAttribute('data-title') || '';
                const year = card.getAttribute('data-year') || '';
                const desc = card.getAttribute('data-desc') || '';
                const categoryStr = card.getAttribute('data-category') || '';
                const toolsStr = card.getAttribute('data-tools') || '';
                const imgsAttr = card.getAttribute('data-imgs') || card.getAttribute('data-img') || '';
                
                slideImages = imgsAttr.split(',').map(s => s.trim()).filter(Boolean);
                currentSlide = 0;

                document.getElementById('detail-modal-title').textContent = title;
                document.getElementById('detail-modal-year').textContent = year;
                document.getElementById('detail-modal-desc').textContent = desc;

                const catContainer = document.getElementById('detail-modal-categories');
                catContainer.innerHTML = categoryStr.split(',').map(c => 
                    `<span class="px-2.5 py-1 bg-white/10 border border-white/15 rounded-full text-xs text-white/80 font-mono">${c.trim()}</span>`
                ).join('');

                const toolsContainer = document.getElementById('detail-modal-tools');
                toolsContainer.innerHTML = toolsStr.split(',').map(t => 
                    `<span class="px-2.5 py-1 bg-white/10 border border-white/15 rounded-full text-xs text-white/80 font-mono">${t.trim()}</span>`
                ).join('');

                const track = document.getElementById('modal-slides-track');
                if (track) {
                    track.innerHTML = slideImages.map(img => 
                        `<img src="${img}" class="w-full h-full object-cover flex-shrink-0" alt="${title}">`
                    ).join('');
                }

                const dotsContainer = document.getElementById('slider-dots');
                if (dotsContainer) {
                    dotsContainer.innerHTML = slideImages.map((_, idx) => 
                        `<button class="slider-dot h-2 rounded-full transition-all duration-300 ${idx === 0 ? 'bg-white w-6' : 'bg-white/40 w-2'}" data-index="${idx}"></button>`
                    ).join('');

                    document.querySelectorAll('.slider-dot').forEach(dot => {
                        dot.addEventListener('click', (ev) => {
                            currentSlide = parseInt(ev.target.getAttribute('data-index'));
                            updateSlider();
                            startAutoSlide();
                        });
                    });
                }

                updateSlider();
                if (modal) {
                    modal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
                startAutoSlide();
            });

            document.getElementById('slider-prev-btn')?.addEventListener('click', () => {
                if (slideImages.length <= 1) return;
                currentSlide = (currentSlide - 1 + slideImages.length) % slideImages.length;
                updateSlider();
                startAutoSlide();
            });

            document.getElementById('slider-next-btn')?.addEventListener('click', () => {
                if (slideImages.length <= 1) return;
                currentSlide = (currentSlide + 1) % slideImages.length;
                updateSlider();
                startAutoSlide();
            });

            document.getElementById('close-detail-modal-btn')?.addEventListener('click', () => {
                if (modal) {
                    modal.classList.remove('active');
                    document.body.style.overflow = '';
                }
                stopAutoSlide();
            });

            // Close on outside click
            modal?.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.remove('active');
                    document.body.style.overflow = '';
                    stopAutoSlide();
                }
            });

            // Close on escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && modal?.classList.contains('active')) {
                    modal.classList.remove('active');
                    document.body.style.overflow = '';
                    stopAutoSlide();
                }
            });
        });
    </script>
</body>
</html>
'''

with open('karya.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("KARYA REBUILT SUCCESSFULLY!")
