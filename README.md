> ## About this fork
>
> This is a personal fork of [FossifyOrg/Calendar](https://github.com/FossifyOrg/Calendar) that gives
> the month grid the Japanese-calendar treatment: a blue Saturday, a red Sunday, and the Japanese
> public holidays coloured like Sundays.
>
> ### Changes made in this fork
>
> - The single "Color of highlighted weekends" setting is split into **Saturday color** and **Sunday
>   color**, each with its own colour picker. Existing installs keep their old colour as the Sunday
>   colour; Saturday defaults to blue.
> - A **Highlight Japanese public holidays** setting (on by default) colours the national holidays
>   with the Sunday colour, so one picker drives both. A holiday outranks the weekday it falls on, so
>   a Saturday holiday reads red rather than blue.
> - The holiday table lives in `app/src/main/res/raw/japanese_holidays.csv`, generated from the
>   Cabinet Office's official list by `tools/UpdateJapaneseHolidays.py`. It has to be regenerated once
>   a year — the equinox holidays only become law in February of the preceding year — and days outside
>   the table are simply left uncoloured. No network access is added to the app.
> - The monthly view and the monthly widget paint a faint tint (15% of the chosen colour) behind each
>   weekend and holiday cell. The tint is derived from the picked colour rather than hard-coded, so it
>   stays readable in both the light and the dark theme.
> - The weekly view, the yearly view and the widget configuration preview follow the same colours, so
>   nothing is left using a single shared weekend colour.
> - Debug builds are labelled `Calendar (JP)` so the fork can be installed alongside an upstream build.
>
> Everything else is unchanged. Like the original, this fork is licensed under the
> [GNU General Public License v3.0](LICENSE).

# Fossify Calendar
<img alt="Logo" src="graphics/icon.webp" width="120" />

<a href='https://play.google.com/store/apps/details?id=org.fossify.calendar'><img alt='Get it on Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png' height=80/></a> <a href="https://f-droid.org/packages/org.fossify.calendar/"><img src="https://fdroid.gitlab.io/artwork/badge/get-it-on-en.svg" alt="Get it on F-Droid" height=80/></a> <a href="https://apt.izzysoft.de/fdroid/index/apk/org.fossify.calendar"><img src="https://gitlab.com/IzzyOnDroid/repo/-/raw/master/assets/IzzyOnDroid.png" alt="Get it on IzzyOnDroid" height=80/></a>

Your Private & Powerful Schedule Planner

Tired of cluttered calendars and privacy concerns?

Fossify Calendar is here to change that. Your open-source powerhouse for managing life, designed with privacy as its core and packed with powerful features to keep you organized.

Here's what makes Fossify Calendar different:

**🚫 AD-FREE AND PRIVATE:**  
Your events remain yours. No ads, no tracking, no intrusive permissions.

**⏰ FLEXIBLE AND CUSTOMIZABLE:**  
Craft events precisely with times, durations, reminders, and advanced repetition rules.

**🔄 SEAMLESS SYNCING:**  
Sync effortlessly with Google Calendar, Outlook, Nextcloud, Exchange, and more.

**🎨 PERSONALIZE YOUR PLANNER:**  
Set custom sounds, looping audio streams, vibrations, and themes to match your preferences.

**🌈 VIBRANT WIDGETS:**  
Brighten your day with beautiful calendar widgets and themes for your home screen.

**📅 EFFORTLESS DAY MANAGEMENT:**  
Plan your day with ease, whether you're a busy professional or a family organizer.

**🎉 IMPORT CELEBRATIONS:**  
Never miss a birthday or anniversary! Easily import holidays and special dates.

**🔍 FILTER VIEWS:**  
Quickly find what you're looking for with event filters.

**📆 MULTIPLE VIEWS:**  
Switch between daily, weekly, monthly, yearly, and event views effortlessly.

**✨ MATERIAL DESIGN ELEGANCE:**  
Enjoy an intuitive and user-friendly interface with dynamic themes.

**Plus, Fossify Calendar is open-source!**

Join the vibrant community on GitHub, contribute to the project, and make it uniquely yours.

Download Fossify Calendar now and experience the power of a private and customizable schedule.

➡️ Explore more Fossify apps: https://www.fossify.org<br>
➡️ Open-Source Code: https://www.github.com/FossifyOrg<br>
➡️ Join the community on Reddit: https://www.reddit.com/r/Fossify<br>
➡️ Connect on Telegram: https://t.me/Fossify

<div align="center">
<img alt="App image" src="fastlane/metadata/android/en-US/images/phoneScreenshots/1_en-US.png" width="30%">
<img alt="App image" src="fastlane/metadata/android/en-US/images/phoneScreenshots/2_en-US.png" width="30%">
<img alt="App image" src="fastlane/metadata/android/en-US/images/phoneScreenshots/4_en-US.png" width="30%">
</div>
