with open('karya.html', 'r', encoding='utf-8') as f:
    html = f.read()

before = html[:html.find('<!-- ✨ PROJECT DETAIL MODAL')]

missing_html = '''
                                <div class="relative w-full lg:w-[40%] mt-8 lg:mt-0 lg:-ml-12 lg:translate-y-12 z-30 px-6 sm:px-12 lg:px-0">
                                    <div class="bg-[#090212]/95 backdrop-blur-md border border-white/10 shadow-[10px_10px_0_rgba(0,0,0,1)] p-6 sm:p-8 rotate-3 group-hover:rotate-0 transition-transform duration-500 pointer-events-auto">
                                        <p class="text-gray-300 font-sans text-sm sm:text-base leading-relaxed">
                                            Riset dan implementasi pembuatan UI/UX dan assets pada proyek game Trash City.
                                        </p>
                                        <div class="mt-4 flex flex-wrap gap-2 text-xs font-mono text-yellow-400">
                                            <span class="px-2 py-1 bg-yellow-400/10 border border-yellow-400/30">Photoshop</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

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
'''

after = html[html.find('    <!-- ✨ PROJECT DETAIL MODAL'):]
after = after.replace('    <!-- ✨ PROJECT DETAIL MODAL WITH 3-IMAGE CAROUSEL & AUTO-SLIDE ✨ -->\n', '')

with open('karya.html', 'w', encoding='utf-8') as f:
    f.write(before + missing_html + after)

print("Fixed.")
