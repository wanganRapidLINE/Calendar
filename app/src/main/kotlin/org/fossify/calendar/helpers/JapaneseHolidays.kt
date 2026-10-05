package org.fossify.calendar.helpers

import android.content.Context
import org.fossify.calendar.R

// The Cabinet Office holiday table bundled in res/raw, keyed by the same dayCode strings
// (yyyyMMdd) the rest of the app uses, so a lookup needs no date parsing at all.
// Regenerate it with tools/UpdateJapaneseHolidays.py once a year - see that script for why.
object JapaneseHolidays {
    @Volatile
    private var holidays: Map<String, String>? = null

    fun isHoliday(context: Context, dayCode: String) = getHolidays(context).containsKey(dayCode)

    fun getHolidayName(context: Context, dayCode: String): String? = getHolidays(context)[dayCode]

    private fun getHolidays(context: Context) = holidays ?: synchronized(this) {
        holidays ?: load(context).also { holidays = it }
    }

    private fun load(context: Context) = try {
        context.resources.openRawResource(R.raw.japanese_holidays)
            .bufferedReader()
            .useLines { lines ->
                lines.mapNotNull { line ->
                    val separator = line.indexOf(',')
                    if (separator == -1) {
                        null
                    } else {
                        line.substring(0, separator) to line.substring(separator + 1)
                    }
                }.toMap()
            }
    } catch (e: Exception) {
        // a missing or unreadable table just means no day is ever a holiday
        emptyMap()
    }
}
