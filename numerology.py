# This program adds together Birthday numbers provided by the user to determine his Life Path Number.
# The descriptions are written by Felicia Bender and come from www.astrostyle.com

print("Hello :)")
print("In order to calculate your Life Path Number please answer the following questions:")

# Store input numbers
year = input("Enter your Birth Year:")
month = input("Enter your Birth Month:")
day = input("Enter your Birth Day:")

# Add Day + Month + Year
birthdate = int(day) + int(month) + int(year)

digits = [int(x) for x in str(birthdate)]

a = sum(digits)

b = [int(x) for x in str(a)]

number = sum(b)

# Display the sum

print("Your Number is: ")
print(number)

# Display the description of each number

if number == 1 or number == 10:
    print(""" 1 Life Path: The Leader
          As a 1 Life Path, your purpose is to develop and master innovative creativity, confidence, independence, originality, and achievement.
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging obstacles to overcome as you master your life’s purpose.
          
          What are you totally passionate about and how can you express it using your unique voice? As a 1, you’re here to act upon your creative ideas and to step forward as a leader.
          Your happiness lies in believing in yourself and what you’re passionate about—not what other people think you “should” be doing.
          Once you identify your areas of strength, dive in with gusto and hone your innovative and unique ideas. No need to follow the flock!
          Your success resides in taking risks and trusting your gut, even if others find your vision weird or eccentric at first. That fine, since you’re not meant to color inside the lines anyway!
          As a natural leader and innovator, embrace the idea of becoming an entrepreneur while also making sure you get the foundational skills required to achieve success on your own terms.
          Once you’ve mastered the basics, get out there and take charge! Your highest and best self is often revealed when you get your creative ideas up and running, then move on to the next idea.
          Just remember to circle back to tend to what you’ve already launched instead of leaving a million fires burning. Doing so will be further fuel for your next endeavor.
          
          When In Alignment, You Are:
          Innovative, energetic, original thinker, leader, determined, inspired, courageous.
          
          When Out of Alignment, You Can Become:
          Self-important, domineering, intolerant, insecure, helpless, victimized, wishy-washy, self-destructive
          
          The Message:
          You’re here to learn how to individuate yourself from others, develop healthy independence, and get on the road to attainment and achievement.
          March to the beat of a different drummer while avoiding any tendencies toward self-absorption.
          Work on quieting the critical voice that plays in your head 24/7—the one telling you you’re not good enough, not smart enough, not worthy, or whatever other lies and propaganda it whispers.
          Don’t be afraid to “fail forward,” by taking big chances and learning as you go.
          You’re meant to manifest your unique ideas in the world.
          """)
elif number == 2 or number == 20:
    print("test")
elif number == 3 or number == 30:
    print("")
elif number == 4 or number == 40:
    print("")
elif number == 5 or number == 50:
    print("""5 Life Path: The Freedom Seeker
          As a 5 Life Path, your purpose is to develop fearlessness, adventurousness, resilience, and the constructive use of freedom.
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging lessons that will guide you towards mastering your life’s purpose.
          
          Can you embrace (and enjoy!) the fact that you are meant to explore the world and be adventurous? As a 5, you’re here to experience life in all of its tactile glory.
          You’re at your best when you can tap into a fearless sense of adventure, use your versatility in a focused and dynamic way, and see the world as your oyster.
          A standard 9-5 job probably won’t cut it for your versatile personality. You need a career with tons of freedom, that allows you to travel, explore or indulge your adventurous spirit.
          And be sure to give yourself permission to experience the world before you settle down into anything permanent. The house, a family, the marriage—that can come later.
          As the number of excesses, beware of going overboard with partying or hedonistic indulgences.
          
          When In Alignment, You Are:
          Freedom-loving, adventurous, fearless, resilient, an agent of change, flexible, fun
          
          When Out Of Alignment, You May Become:
          Indulgent, excessive, restless, emotionally volatile, prone to addiction, fearful, melancholic, procrastinating, erratic, easily overwhelmed
          
          The Message:
          You’re an agent of change and the master of progressive thought and action. Key themes are freedom, fun, fearlessness, and adventure.
          You’re here to experience all that this rich and bountiful planet has to offer—within healthy and focused perimeters.
          Your nemesis? Attracting restrictive circumstances into your life and working through lots of fear.
          Your mantra may as well be, “Don’t fence me in!”
          """)
elif number == 6 or number == 60:
    print("")
elif number == 7 or number == 70:
    print("")
elif number == 8 or number == 80:
    print(""" 8 Life Path: The Powerhouse
          As an 8 Life Path, your purpose is to develop an empowered relationship with money, power, control, and authority.
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging lessons that will guide you towards mastering your life’s purpose.

          How can you embrace the fact that you’re meant to think big and be a financial success? As an 8, you’re destined to make a big splash in the world of money, power, control, and authority.
          Yet it may not be an easy dash to get there! You need to tap into your sense of personal power—one that could be tested from very early on in life.
          Once you get a handle on that, you will begin to attract and create lasting wealth. But your path to riches won’t necessarily be linear. You may go up, down and all around before you find your formula for success.
          Along the way, authority issues will need to be balanced.
          Be resilient. Focus on your goal and move toward it with savvy management, organization, fortitude, heart, and most of all, integrity.

          When In Alignment, You Are:
          Financially abundant, authoritative, powerful, in control, influential, giving

          When Out Of Alignment, You May Become:
          Self-centered, controlling, opinionated, materialistic, forceful, rebellious, passive, victimized, powerless, insecure, scarcity-minded, blaming

          The Message:
          You’re here to master the art of success in the material world. Think big and go for it. The 8 is the number of manifestation.
          What you focus on with clear intent, integrity, and effort can magically manifest with amazing power.
          """)
elif number == 9 or number == 90:
    print("")
elif number == 11:
    print("")
elif number == 22:
    print("")
elif number == 33:
    print("")                                           
else:
    print("THE END")
