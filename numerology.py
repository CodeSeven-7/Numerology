# This program adds together Birthday numbers provided by the user to determine his Life Path Number.
# The descriptions are written by Felicia Bender and come from www.astrostyle.com

print('Finding Meaning In Numbers')
print("Numerology can be used to help us to better understand the world and ourselves as individuals where you can discover insights about your purpose and personality traits.")
print("Would you like to know your Life Path Number?")

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
    print(""" 5 Life Path: The Freedom Seeker
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
    print(""" 7 Life Path: The Seeker
          As a 7 Life Path, your purpose is to develop your intuition, spirituality, trust, and openness, balanced against your desire for data-driven analysis
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging lessons that will guide you towards mastering your life’s purpose.

          Can you accept that you’re both an intellectual and a psychic?
          As a 7, you’re always seeking answers to life’s big (and small) questions.
          You live mostly in your head and tend to over-intellectualize everything.
          You’re learning how to manage and understand the emotional side of life.
          You’re actually quite a sensitive and emotional person, yet that part of you feels foreign.
          Understand that you’re on a different wavelength than most people.
          You’re great with any career in which you can work alone for part of the time—research, science, data collecting, computers.
          Yet you can also feel the pull of your more intuitive side and be drawn to the healing arts, metaphysical thought, and self-exploration.

          When In Alignment, You Are:
          Data-driven & analytical, refined mind, knowledge-driven, intuitive, wise, truth-seeker, spiritually centered.

          When Out Of Alignment, You May Become:
          Critical, obsessive, secretive, distrustful, pessimistic, intimidating, always “in your head” OR superficial, overly trusting, ignorant, easily frustrated.

          The Message:

          You’re here to be a Truth Seeker—your life is spent developing and acknowledging both the left/right brain continuum in yourself.
          When you tap in to both your analytical brain and your intuitive brain, you’re at your most powerful.
          You’re on an “internal journey” seeking to know who you really are—deep down at your core. You need “alone” time.
          """)
elif number == 8 or number == 80:
    print(""" 8 Life Path: The Powerhouse
          As an 8 Life Path, your purpose is to develop an empowered relationship with money, power, control, and authority.
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging lessons that will guide you towards mastering your life’s purpose.

          How can you embrace the fact that you’re meant to think big and be a financial success? As an 8, you’re destined to make a big splash in the world of money, power, control, and authority.
          Yet it may not be an easy dash to get there! You need to tap into your sense of personal power—one that could be tested from very early on in life.
          Once you get a handle on that, you will begin to attract and create lasting wealth. But your path to riches won’t necessarily be linear.
          You may go up, down and all around before you find your formula for success.
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
    print(""" 9 Life Path: The Humanitarian
          As a 9 Life Path, your purpose is to develop your spirituality, humanitarianism, creativity, wisdom, and integrity
          These themes will be reoccurring issues throughout your life, as your Life Path number indicates what you’re evolving into, developing, aspiring toward, and learning about.
          While you’ll display innate gifts and talents in these areas, you’ll also experience some challenging lessons that will guide you towards mastering your life’s purpose.

          How can you best go with the flow of your creative and giving impulses? As a 9, you’re versatile and unique.
          While you can be successful at virtually anything you feel passionate about, you may feel most fulfilled when serving a humanitarian cause—large or small.
          Creative, compassionate and giving, it’s through blending your gifts of imagination with your spirit of service that you truly find your groove.
          It’s merely a lack of concentration that can keep you from enjoying the success of your projected goals.
          Your challenge lies in learning to ask for support instead of struggling alone or falling into martyrdom.
          You’re naturally generous and more comfortable in the role of the giver, but your path involves learning how to receive.
          At times, you may hold on to the past. Challenge yourself to surrender and master the fine art of letting go.

          When In Alignment, You Are:
          Humanitarian, compassionate, magnetic, charitable, romantic, creative, generous, idealistic

          When Out of Alignment, You Can Be:
          Resentful, unable to let go of grudes and toxic emotions, hostile, haughty, close-minded, submissive, emotionally unavailable, drifting, deceptive, lacking healthy boundaries

          The Message:
          With your divinely inspired creative approach, you are here to make a profound difference in the world.
          Throughout your life, you may devour books and studies involving spirituality or psychology.
          On a personal level, you’re learning how to express and understand your own deep (and sometimes confusing) feelings.
          As you master and digest this information, avoid proselytizing.
          Instead, work towards becoming an objective listener and empowering supporter of others on a similar path.
          """)
elif number == 11:
    print("")
elif number == 22:
    print("")
elif number == 33:
    print("")                                           
else:
    print("THE END")
