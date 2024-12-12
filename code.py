from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Create a console for colorful output
console = Console()

# Define the Christmas tree graphic
christmas_tree = """
         *                                *                                *                            *                         *
        /|\\                              ***                              /-\\                          /~\\                       /o\\
       /*|O\\                            *****                            /^*^\\                        /***\\                     /*~*\\
      /*/|\*\\                          *******                          /*^*^*\\                      /~~~~~\\                   /ovovo\\
     /X/O|*\X\\                        *********                        /^*^*^*^\\                    /^^^^^^^\\                 /~*~*~*~\\
    /*/X/|O\X*\\                      ***********                      /*^*^*^*^*\\                  /---------\\               /xoxoxoxox\\
   /O/X/*|X\O*\\                     *************                    /^*^*^*^*^*^\\                /*^-*^-*^-*^\\             /^~^~^~^~^~^\\
        |-|                              |=|                              |||                          |"|                       |`|
        |-|                              |=|                              |||                          |"|                       |`|
"""

# Define the invitation message
invitation_message = (
    "🎄✨ Important information for our Christmas Dinner! ✨🎄\n"
    "\n"
    "📅 Date: December 15th\n"
    "⏰ Time: for i in range(10 PM) or 6:00 PM :)\n"
    "📍 Location: Meet up somewhere close to Majorstuen and then we can walk to a cozy place all together.\n"
    "\n"
    "Let's celebrate the end of our internship with drinks and/or delicious food! 🍽️\n"
    "Jeffrey you can't say no!!! 🎅\n"
)

# Create a styled text for the invitation
styled_message = Text(invitation_message, style="bold green on black")

# Display the Christmas tree and message
console.print(Panel(christmas_tree, title="Merry Christmas!", subtitle="2024", style="bold red"))
console.print(Panel(styled_message, border_style="green", style="bold"))
