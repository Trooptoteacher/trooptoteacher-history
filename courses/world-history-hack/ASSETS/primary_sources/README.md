# Primary-Source Image Bank — World History Hack

One genuine **public-domain** primary source per standard (92 total). Full sourcing detail (work, creator, year, repository, page URL, rights, search hint) is in `../../05_STANDARDS_ALIGNMENT/primary_source_sourcing.json`.

## How to pull each image
1. Open the source's `page_url` (a real repository page).
2. Use the repository's **Original file / Download** control to get the full-res file (the direct link isn't pre-filled because the build sandbox can't reach image hosts).
3. Confirm the rights line (must be pre-1929 PD, US-gov, or CC0).
4. Save it with the **exact** filename in `EXPECTED_FILENAMES.txt`, e.g. `W.14_slug.jpg`.
5. Put all files in the Drive **World History Hack** folder; re-export anything >10 MB to ≤10 MB (~2000 px); prefer ≥~1200 px.
6. Then `python3 ../../BUILD/engine/sync_images.py` fans them into every deck/unit/web asset folder.

## Status: 89/92 have a search-verified repository page; 3 need a manual source pick (see `search_hint`).

| Std | Unit | Type | Work | Rights | Verified page |
|---|---|---|---|---|---|
| W.01 | 1 | painting | Portrait of Louis XIV in Coronation Robes | Public domain (pre-1929) | ✅ |
| W.02 | 1 | manuscript | Magna Carta (1215) - BL Cotton MS Augustus II 10 | Public domain (pre-1929) | ✅ |
| W.03 | 1 | painting | Portrait of John Locke | Public domain (pre-1929) | ✅ |
| W.04 | 1 | painting | The Execution of Charles I | Public domain (pre-1929) | ✅ |
| W.08a | 1 | document | Engrossed Declaration of Independence, front | PD-US-gov (US National Archives) | ✅ |
| W.05 | 2 | political cartoon | A faut esperer q'eu jeu la finira bentot (Third  | Public domain (published 1789, pre-1929; PD-old in country of origin) | ✅ |
| W.06 | 2 | painting | Prise de la Bastille (The Storming of the Bastil | Public domain (Houel 1735-1813, published 1789, pre-1929; PD-old) | ✅ |
| W.07 | 2 | painting | Napoleon Crossing the Alps (Bonaparte franchissa | Public domain (David 1748-1825, painted 1801, pre-1929; PD-old) | ✅ |
| W.08b | 2 | painting | Declaration of the Rights of Man and of the Citi | Public domain (Le Barbier 1738-1826, c.1789, pre-1929; PD-old) | ✅ |
| W.09 | 2 | engraving | General Toussaint Louverture | Public domain (published before January 1, 1931, pre-1929; PD-old) | ✅ |
| W.10 | 3 | engraving | Jethro Tull seed drill (1762) | Public domain (published 1762, pre-1929) | ✅ |
| W.11 | 3 | painting | Coalbrookdale by Night | Public domain (painted 1801, pre-1929) | ✅ |
| W.12 | 3 | map | Cheffins's Map of English & Scotch Railways, 185 | Public domain (published 1850, pre-1929) | ✅ |
| W.13 | 3 | diagram | Stowage of the British slave ship Brookes under  | Public domain (published 1788; Library of Congress, no known restrictions on publication) | ✅ |
| W.14 | 3 | engraving | Stephenson's Rocket drawing (Mechanics Magazine, | Public domain (published 1829, pre-1929; PD-Mark) | ✅ |
| W.15 | 3 | photograph | Pennsylvania breaker boys, 1911 | Public domain (taken 1911, pre-1929; PD-NCLC, no known restrictions) | ✅ |
| W.16 | 3 | document | Manifesto of the Communist Party (first edition  | Public domain (published 1848, pre-1929; PD-Mark) | ✅ |
| W.17 | 4 | painting | Kaiserproklamation im Spiegelsaal von Versailles | Public domain (pre-1929; artist died 1915) | ✅ |
| W.18 | 4 | newspaper front page | "J'accuse...!" front page of L'Aurore, Emile Zol | Public domain (pre-1929; published 1898) | ✅ |
| W.19 | 5 | political cartoon | The Rhodes Colossus | Public domain (published in Punch, 10 December 1892; pre-1929) | ✅ |
| W.20 | 5 | map | African map 1885 | Public domain (pre-1929; author life+70) | ✅ |
| W.21 | 5 | engraving/illustration | Berlin Conference, 1884-85 | Public domain (period engraving, 1884; pre-1929) | ✅ |
| W.22 | 5 | photograph | Emperor Menelik II | Public domain (photograph c.1900s; pre-1929) | ✅ |
| W.23 | 6 | engraving/illustration | The Sepoy revolt at Meerut (Illustrated Times, 1 | Public domain (pre-1929; PD-old, expired copyright) | ✅ |
| W.24 | 6 | engraving/painting | Destroying Chinese war junks, by E. Duncan (1843 | Public domain (PD-old-100-expired; CC-PD-Mark) | ✅ |
| W.25 | 6 | photograph | Yule Island missionaries, 1892 | Public domain (pre-1929; author's life+70 expired) | ✅ |
| W.26 | 6 | woodblock print | Japanese 1854 print of Commodore Perry | Public domain (pre-1929; PD-old) | ✅ |
| W.27 | 6 | photograph | Panama Canal construction, 1907-10 | Public domain (Library of Congress; no known copyright restrictions) | ✅ |
| W.28 | 6 | illustration | Banana plantation (Popular Science Monthly, vol. | Public domain (pre-1929; from Popular Science Monthly) | ✅ |
| W.29 | 7 | map | Map of European Alliances, 1914 (from Shepherd's | Public domain (pre-1929; derived from William Shepherd, Historical Atlas, 1911) | ✅ |
| W.30 | 7 | illustration | Assassination of Archduke Franz Ferdinand at Sar | Public domain (PD-old-80-expired) | ✅ |
| W.31 | 7 | photograph | Cheshire Regiment in a trench at the Somme, 1916 | Public domain (UK Crown copyright expired; official WWI photograph) | ✅ |
| W.32 | 7 | map | Battle of Verdun: Verdun and Vicinity, 21 Februa | Public domain (work of the U.S. Government / USMA) | ✅ |
| W.33 | 7 | document | Zimmermann Telegram as Received by the German Am | Public domain (NARA; CC-PD-Mark) | ✅ |
| W.34 | 7 | photograph | Women Working in the Munitions Industry during t | Public domain (PD-UKGov) | ✅ |
| W.35 | 7 | photograph | Starvation during the Armenian Genocide | Public domain (Wikimedia Commons; 1915-16 photograph) | ✅ |
| W.36 | 7 | painting | The Signing of Peace in the Hall of Mirrors, Ver | Public domain (PD-old; artist died 1931) | ✅ |
| W.37 | 7 | map | Map of Europe in 1919 (after the Treaties of Bre | Public domain (pre-1929; London Geographical Institute, 1919) | ✅ |
| W.38 | 7 | photograph | Lenin delivering a speech in Red Square, Moscow  | Public domain (pre-1929 photograph) | ✅ |
| W.39 | 8 | photograph | Col. Charles Lindbergh (Spirit of St. Louis tran | PD-US: published 1927 (pre-1929), US copyright expired | ✅ |
| W.40 | 8 | photograph | Crowds gathering outside the New York Stock Exch | PD-US: published 1929, US copyright expired (labeled PD US expired) | ✅ |
| W.41 | 8 | photograph | Hyperinflation in Germany, 1923 (Weimar Republic | Creative Commons Public Domain Mark 1.0 (PD-marked) | ✅ |
| W.42 | 8 | photograph | March on Rome, 1922 - Benito Mussolini | PD: published 1922 (pre-1929), anonymous/Illustrazione Italiana; US copyright expired | ✅ |
| W.43 | 8 | map | Map of Europe 1914 (United States Military Acade | PD: U.S. Government work (US Military Academy / US Defense Printing Agency) | ✅ |
| W.44 | 8 | photograph | Second Italo-Ethiopian War (Italian invasion of  | Wikimedia Commons - PD basis not confirmed in search (verify Italian pre-1976 government/anonymous status before use) | ⬜ |
| W.49 | 8 | photograph | Nazi boycott of Jewish businesses, Berlin, April | No known copyright (US Holocaust Memorial Museum / U.S. National Archives) | ✅ |
| W.45 | 9 | photograph | Neville Chamberlain holding the Anglo-German Dec | Wikimedia Commons: no known copyright restrictions / public domain | ✅ |
| W.46 | 9 | photograph | 19th Bombardment Group B-29 Superfortress, World | Public domain — work of the U.S. federal government (US Army Air Forces) | ✅ |
| W.47 | 9 | photograph | Into the Jaws of Death — U.S. troops landing at  | Public domain — work of the U.S. federal government (U.S. Coast Guard) | ✅ |
| W.48 | 9 | photograph | Winston Churchill outside 10 Downing Street, 21  | Public domain — UK Government work (Crown copyright expired) | ✅ |
| W.50 | 9 | photograph | Slave laborers in the Buchenwald concentration c | Public domain — work of the U.S. federal government (U.S. Army Signal Corps); NARA archival record | ✅ |
| W.51 | 9 | photograph | The Big Three (Churchill, Roosevelt, Stalin) at  | Public domain — work of the U.S. federal government (U.S. Army) | ✅ |
| W.52 | 9 | photograph | Y-12 Calutron operators ('Calutron Girls') at Oa | Public domain — work of the U.S. federal government (Manhattan Project, U.S. Army/DOE) | ✅ |
| W.53 | 9 | photograph | Nuremberg Trials — looking down on the defendant | Public domain — work of the U.S. federal government (U.S. Army); NARA record | ✅ |
| W.54 | 10 | propaganda poster | Marshall Plan poster ('Whatever the weather, we  | Public domain - work of the U.S. Federal Government (Economic Cooperation Administration); PD Mark 1.0 on Commons | ✅ |
| W.55 | 10 | photograph | David Ben-Gurion proclaiming the Declaration of  | Public domain - marked PD on Commons (Israeli copyright term for photographs expired) | ✅ |
| W.56a | 10 | photograph | Joseph Stalin, Winston Churchill and President T | Public domain - PD US Government (category 'PD US Government' on Commons) | ✅ |
| W.56b | 10 | photograph | Emperor Hirohito and General MacArthur, first me | Public domain - photograph by a U.S. federal employee (Army photographer Gaetano Faillace) | ✅ |
| W.57 | 10 | photograph | Mao Zedong proclaiming the establishment of the  | Public domain - marked 'PD China' on Commons (Chinese copyright term expired) | ✅ |
| W.58 | 10 | photograph | C-54 Skymaster landing at Berlin Tempelhof durin | Public domain - work of the U.S. Federal Government (U.S. Air Force), PD US Government on Commons | ✅ |
| W.59 | 10 | photograph | President Harry S. Truman signing the North Atla | Public domain - work of the U.S. Federal Government (Truman Library), PD Mark 1.0 on Commons | ✅ |
| W.60 | 11 | photograph | US Army tanks face off against Soviet tanks, Ber | Public domain — work of the U.S. Army (U.S. federal government) | ✅ |
| W.61 | 11 | photograph | President Nixon and General Secretary Brezhnev s | Public Domain Mark 1.0 — White House Photo Office (U.S. federal government) | ✅ |
| W.62 | 11 | photograph | Soviet tank in Budapest 1956 (Hungarian Revoluti | Public domain — PD-CIA (U.S. federal government) | ✅ |
| W.63a | 11 | photograph | General MacArthur observing the naval shelling o | Public domain — work of the U.S. armed forces (U.S. federal government) | ✅ |
| W.63b | 11 | photograph | U.S. UH-1 Huey helicopter spraying Agent Orange  | Public domain — work of the U.S. Army (U.S. federal government) | ✅ |
| W.64 | 11 | photograph | President Reagan and General Secretary Gorbachev | Public domain — NARA / White House Photographic Office (U.S. federal government) | ✅ |
| W.65 | 11 | map | Soviet Union — Administrative Divisions, 1989 (C | Public domain — PD-USGov (CIA map published by the U.S. Government Printing Office) | ✅ |
| W.66 | 12 | photograph | Emergency trains crowded with desperate refugees | Public domain (Partition of India, 1947; listed as public domain / PD-India on Wikimedia Commons) | ✅ |
| W.67 | 12 | photograph | Muhammad Ali Jinnah speaking on 14 August 1947 | Public domain - copyright expired (PD-Pakistan / PD-India; pre-1958 anonymous South Asian work) | ✅ |
| W.68 | 12 | photograph | Jawaharlal Nehru delivering his 'Tryst with Dest | Public domain (PD-India; published 1947, Indian Copyright Act 1957) | ✅ |
| W.69 | 12 | photograph | President Gamal Abdel Nasser of Egypt | Public domain (PD Egypt, per Wikimedia Commons file page) | ✅ |
| W.70 | 12 | photograph | F.W. de Klerk (last apartheid-era president) and | Library of Congress, Carol M. Highsmith Archive - no known copyright restrictions | ✅ |
| W.71 | 12 | photograph | Mobutu Sese Seko of Zaire meeting President Rich | Public domain (PD-USGov; work of the U.S. Federal Government) | ✅ |
| W.72 | 12 | photograph | Fidel Castro during his 1959 visit to Washington | Library of Congress, U.S. News & World Report Magazine Photograph Collection - no known restrictions on publication | ✅ |
| W.73 | 12 | map | 1993 CIA map of the former Yugoslavia | Public domain (PD-USGov-CIA; work of the U.S. Central Intelligence Agency) | ✅ |
| W.74 | 12 | photograph | Remains of victims of the 1994 Rwandan genocide  | Creative Commons Public Domain Mark 1.0 (documentary photograph of the 1994 massacre site) | ✅ |
| W.75 | 12 | photograph | President Ronald Reagan making his 'tear down th | Public domain (PD-USGov; White House / U.S. Federal Government work) | ✅ |
| W.76 | 12 | photograph | Sadat, Carter, and Begin handshake at the Camp D | Library of Congress, U.S. News & World Report Magazine Photograph Collection - no known restrictions on publication | ✅ |
| W.77 | 13 | chart | New York population pyramid | CC0 Public Domain Dedication (per search result) | ✅ |
| W.78 | 13 | chart | Population pyramid of Japan 2015 | Public Domain Mark 1.0 / work of the U.S. federal government (per search result) | ✅ |
| W.79 | 13 | diagram | NHGRI human male karyotype | Public domain, work of the U.S. federal government (NIH/NHGRI) (per search result) | ✅ |
| W.80 | 13 | illustration | GPS Satellite (NASA art, Block IIF) | Public domain, NASA (U.S. government work) | ✅ |
| W.81 | 13 | photograph | Rocks of crack cocaine | Public domain, U.S. DEA (per search result) | ✅ |
| W.82 | 13 | photograph | Container port facilities in Newark Bay | Search asserted NARA/U.S.-gov public domain for Port Newark container images; exact-file PD basis not individually confirmed | ⬜ |
| W.83 | 13 | photograph | U.S. Trade Representative Carla A. Hills at the  | Public domain, work of the U.S. federal government (per search result) | ✅ |
| W.84 | 13 | emblem | Flag of Europe | Public domain on Wikimedia Commons (EU flag/insignia); exact-file PD tag not quoted in search result | ⬜ |
| W.85 | 13 | photograph | Shanghai skyline waterfront Pudong | CC0 Public Domain Dedication (per search result) | ✅ |
| W.86 | 13 | map | Middle East oil and gas (LOC 2007631392) | Public domain, U.S. government map (Library of Congress) (per search result) | ✅ |
| W.87 | 13 | photograph | Power County Wind Farm 002 | Public domain, U.S. Department of Energy (per search result) | ✅ |
| W.88 | 13 | photograph | US Navy F-14A Tomcat flying over burning Kuwaiti | Public domain, U.S. Navy (U.S. government work) (per search result) | ✅ |
| W.89 | 13 | document | The 9/11 Commission Report (complete) | Public Domain Mark 1.0 / U.S. government work (per search result) | ✅ |
