# Historian-Verified Facts — Unit 1 (citation model)

Unit 1 = US.01–US.07, "The Rise of Industrialization," 1877–1900. Every date, number, name,
statute, and case below was verified against primary sources (U.S. Statutes at Large, U.S. Reports,
National Archives, Library of Congress). Use these as the model: NO claim ships unless it can be
cited to a primary source. "No source = cannot verify."

| Fact | Primary-source citation |
|------|-------------------------|
| Homestead Act (1862) | 12 Stat. 392 |
| Pacific Railway Act | 1862 |
| Golden Spike, Promontory Summit, Utah | 1869 |
| Dawes Act | 24 Stat. 388 — signed Feb 8, 1887 by President Cleveland |
| Chinese Exclusion Act | 22 Stat. 58 (1882) |
| Ellis Island opens | 1892 |
| Plessy v. Ferguson | 163 U.S. 537 (1896) |

## Citation discipline for new units

1. Pull the unit narrative and source list from `Trooptoteacher/history-hack-web-app` first.
2. For every numeric/name/date claim on a poster or station, confirm it against a primary source
   (Statutes at Large for laws, U.S. Reports for Supreme Court cases, U.S. Census/BLS for data,
   National Archives / Library of Congress for documents and images).
3. Record the citation in `unitN_content.py` SOURCES and surface a provenance line in the footer
   where appropriate (`footer(c, extra=...)` / `provenance_footer`).
4. If a fact cannot be verified to a primary source, do not publish it — flag it for the user.
