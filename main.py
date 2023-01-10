# class captain system
# by hannah götte

# imports
from guizero import App, Window, Text, Box, Picture, TextBox

# global variables
candidates = []

num_candidates = 0
votes = 0

candidate_one_votes = 0
candidate_two_votes = 0
candidate_three_votes = 0
candidate_four_votes = 0

adding_captain_picture = ""
adding_campaign_poster = ""

end_text = ""

# FUNCTIONS

# add profile window function
def add_profile_window_function():
    global num_candidates
    num_candidates += 1
    if num_candidates > 4:
        main.info("information", "the limit of candidates has already been reached")
    else:
        add_profile_window = Window(main, title="add profile", width=1425, height=825)
        add_profile_window.bg = "white"
        add_profile_window.show(wait=True)
        main.hide()

        # adding in the captain picture
        def add_captain_picture():
            global adding_captain_picture
            adding_captain_picture = add_profile_window.select_file(title="select file", folder=".", filetypes=[["All files", "*"]], save=False, filename="")
            captain_picture_outline.image = adding_captain_picture

        def add_campaign_poster():
            global adding_campaign_poster
            adding_campaign_poster = add_profile_window.select_file(title="select file", folder=".", filetypes=[["All files", "*"]], save=False, filename="")
            campaign_poster_outline.image = adding_campaign_poster

        # add profile save button
        def add_profile_save():
            global candidates, adding_captain_picture, adding_campaign_poster
            if name_textbox.value == "" or campaign_textbox.value == "" or adding_captain_picture == "" or adding_campaign_poster == "":
                add_profile_window.warn("warning", "field(s) are empty, fill in into continue")
            else:
                # saving information to list
                candidates.append(name_textbox.value)
                candidates.append(campaign_textbox.value)
                candidates.append(adding_captain_picture)
                candidates.append(adding_campaign_poster)

                add_profile_window.destroy()
                main.show()

        # top box in add profile window
        add_profile_top_box = Box(add_profile_window, width="fill", height=110)

        # bottom box in add profile window
        add_profile_bottom_box = Box(add_profile_window, width="fill", height=715)

        # add profile top stars
        add_profile_top_left_star = Picture(add_profile_top_box, image="images/star.png", width=110, height=110, align="left")
        add_profile_top_right_star = Picture(add_profile_top_box, image="images/star.png", width=110, height=110, align="right")

        # add profile top box spacer
        add_profile_top_box_spacer = Box(add_profile_top_box, height="fill", width=355, align="left")

        # add profile title
        add_profile_title = Text(add_profile_top_box, text="ADD PROFILE", font="signika", size=90, color="#003566", align="left")

        # add profile boxes
        add_profile_left_box = Box(add_profile_bottom_box, height="fill", width=680, align="left")
        add_profile_left_box_bottom_box = Box(add_profile_left_box, height=110, width="fill", align="bottom")

        add_profile_right_box = Box(add_profile_bottom_box, height="fill", width=680, align="right")
        add_profile_right_box_bottom_box = Box(add_profile_right_box, height=110, width="fill", align="bottom")

        # spacer in add profile window right box
        add_profile_right_box_spacer_one = Box(add_profile_right_box, width="fill", height=80, align="top")

        # add profile bottom stars
        add_profile_bottom_left_star = Picture(add_profile_left_box_bottom_box, image="images/star.png", height=110, width=110, align="left")
        add_profile_bottom_right_star = Picture(add_profile_right_box_bottom_box, image="images/star.png", height=110, width=110, align="right")

        # name box and title
        name_title_box = Box(add_profile_right_box, width="fill", height=50)
        name_title = Text(name_title_box, text="name", font="signika", size=50, color="#003566", align="left")

        # name textbox box
        name_textbox_box = Box(add_profile_right_box, width="fill", height=30)

        # name textbox
        name_textbox = TextBox(name_textbox_box, height=40, width=30, align="left")
        name_textbox.text_color = "black"
        name_textbox.font = "barlow"
        name_textbox.text_size = 20

        # spacer for under name
        add_profile_right_box_spacer_two = Box(add_profile_right_box, width="fill", height=30)

        # campaign box and title
        campaign_title_box = Box(add_profile_right_box, width="fill", height=65)
        campaign_title = Text(campaign_title_box, text="campaign", font="signika", size=50, color="#003566", align="left")

        # campaign textbox box
        campaign_textbox_box = Box(add_profile_right_box, width="fill", height=150)

        # campaign textbox
        campaign_textbox = TextBox(campaign_textbox_box, height=180, width=60, align="left", multiline=True)
        campaign_textbox.text_color = "black"
        campaign_textbox.font = "barlow"
        campaign_textbox.text_size = 20

        # spacer under campaign
        add_profile_right_box_spacer_three = Box(add_profile_right_box, width="fill", height=30)

        # candidate number box
        candidate_no_box = Box(add_profile_right_box, width="fill", height=65, align="top")

        # box inside candidate number box - for the title
        candidate_no_box_box = Box(candidate_no_box, height="fill", width=410, align="left")

        # candidate number title
        candidate_no_title = Text(candidate_no_box_box, text="candidate number: ", font="signika", size=50, color="#003566", align="left")

        # counter
        counter = num_candidates
        counter_text = Text(candidate_no_box, text=counter, font="barlow", size=50, color="#003566", align="left")

        # spacer under candidate number
        add_profile_right_box_spacer_four = Box(add_profile_right_box, width="fill", height=30)

        # adding images
        captain_picture_outline = Picture(add_profile_left_box, image="images/captain picture.png", height=200, width=300)
        campaign_poster_outline = Picture(add_profile_left_box, image="images/campaign poster.png", height=400, width=300)

        # user adding in their images
        captain_picture_outline.when_clicked = add_captain_picture
        campaign_poster_outline.when_clicked = add_campaign_poster

        # add profile save button
        add_profile_save_button = Picture(add_profile_right_box, image="images/save.png", height=80, width=150)
        add_profile_save_button.when_clicked = add_profile_save

# vote window function
def vote_window_function():
    global num_candidates, candidates, votes
    if num_candidates < 2:
        main.info("information", "there are not enough candidates yet to vote")
    elif votes == 30:
        main.info("information", "maximum number of votes have been reached")
    else:
        vote_window = Window(main, title="vote", width=1425, height=825)
        vote_window.bg = "white"
        vote_window.show(wait=True)
        main.hide()

        # counting votes for candidate one
        def candidate_one_vote_function():
            global candidate_one_votes, votes
            votes += 1
            candidate_one_votes += 1

            # pop up letting user know their vote has been saved
            vote_window.info("info", "your vote has been saved")

            # can't go over maximum votes
            if votes == 30:
                vote_window.info("info", "maximum number of votes have been reached")
                vote_window.destroy()
                main.show()

        # counting votes for candidate two
        def candidate_two_vote_function():
            global candidate_two_votes, votes
            votes += 1
            candidate_two_votes += 1

            # pop up letting user know their vote has been saved
            vote_window.info("info", "your vote has been saved")

            # can't go over maximum votes
            if votes == 30:
                vote_window.info("info", "maximum number of votes have been reached")
                vote_window.destroy()
                main.show()

        # counting votes for candidate three
        def candidate_three_vote_function():
            global candidate_three_votes, votes
            votes += 1
            candidate_three_votes += 1

            # pop up letting user know their vote has been saved
            vote_window.info("info", "your vote has been saved")

            # can't go over maximum votes
            if votes == 30:
                vote_window.info("info", "maximum number of votes have been reached")
                vote_window.destroy()
                main.show()

        # counting votes for candidate four
        def candidate_four_vote_function():
            global candidate_four_votes, votes, adding_captain_picture, adding_campaign_poster, candidates
            votes += 1
            candidate_four_votes += 1

            # pop up letting user know their vote has been saved
            vote_window.info("info", "your vote has been saved")

            # can't go over maximum votes
            if votes == 30:
                vote_window.info("info", "maximum number of votes have been reached")
                vote_window.destroy()
                main.show()

        # candidate one info
        def one_info_function():
            global candidates, adding_captain_picture, adding_campaign_poster
            one_info_window = Window(vote_window, title="candidate one", height=400, width=500)
            one_info_window.bg = "white"

            top_box = Box(one_info_window, width="fill", height=50, align="top")
            title = Text(top_box, text="CAMPAIGN", font="signika", size=40, color="#003566")

            spacer = Box(one_info_window, width="fill", height=10, align="top")

            box_one = Box(one_info_window, width="fill", height=200, align="top")

            spacer_two = Box(one_info_window, height=10, width="fill", align="top")

            box_two = Box(one_info_window, width="fill", height=150, align="right")

            one_camp = candidates[1]
            one_text = Text(box_two, text=one_camp, font="barlow", size=20, align="left")

            one_poster = candidates[3]
            one_pic = Picture(box_one, image=one_poster, height=250, width=200)

        # candidate two info
        def two_info_function():
            global candidates, adding_captain_picture, adding_campaign_poster
            two_info_window = Window(vote_window, title="candidate two", height=400, width=500)
            two_info_window.bg = "white"

            top_box = Box(two_info_window, width="fill", height=50, align="top")
            title = Text(top_box, text="CAMPAIGN", font="signika", size=40, color="#003566")

            spacer = Box(two_info_window, width="fill", height=10, align="top")

            box_one = Box(two_info_window, width="fill", height=200, align="top")

            spacer_two = Box(two_info_window, height=10, width="fill", align="top")

            box_two = Box(two_info_window, width="fill", height=150, align="right")

            two_camp = candidates[5]
            two_text = Text(box_two, text=two_camp, font="barlow", size=20, align="left")

            two_poster = candidates[7]
            two_pic = Picture(box_one, image=two_poster, height=250, width=200)

        # candidate three info
        def three_info_function():
            global candidates, adding_captain_picture, adding_campaign_poster
            three_info_window = Window(vote_window, title="candidate three", height=400, width=500)
            three_info_window.bg = "white"

            top_box = Box(three_info_window, width="fill", height=50, align="top")
            title = Text(top_box, text="CAMPAIGN", font="signika", size=40, color="#003566")

            spacer = Box(three_info_window, width="fill", height=10, align="top")

            box_one = Box(three_info_window, width="fill", height=200, align="top")

            spacer_two = Box(three_info_window, height=10, width="fill", align="top")

            box_two = Box(three_info_window, width="fill", height=150, align="right")

            three_camp = candidates[9]
            three_text = Text(box_two, text=three_camp, font="barlow", size=20, align="left")

            three_poster = candidates[11]
            three_pic = Picture(box_one, image=three_poster, height=250, width=200)

        # candidate three info
        def four_info_function():
            global candidates, adding_captain_picture, adding_campaign_poster
            four_info_window = Window(vote_window, title="candidate four", height=400, width=500)
            four_info_window.bg = "white"

            top_box = Box(four_info_window, width="fill", height=50, align="top")
            title = Text(top_box, text="CAMPAIGN", font="signika", size=40, color="#003566")

            spacer = Box(four_info_window, width="fill", height=10, align="top")

            box_one = Box(four_info_window, width="fill", height=200, align="top")

            spacer_two = Box(four_info_window, height=10, width="fill", align="top")

            box_two = Box(four_info_window, width="fill", height=150, align="right")

            four_camp = candidates[13]
            four_text = Text(box_two, text=four_camp, font="barlow", size=20, align="left")

            four_poster = candidates[15]
            four_pic = Picture(box_one, image=four_poster, height=250, width=200)

        # vote save button
        def vote_save():
            global candidate_one_votes, candidate_two_votes, candidate_three_votes, candidate_four_votes
            vote_window.destroy()
            main.show()

        # top box in vote window
        vote_top_box = Box(vote_window, width="fill", height=110, align="top")

        # bottom box in vote window
        vote_bottom_box = Box(vote_window, width="fill", height=715, align="bottom")

        # top stars in vote window
        vote_top_left_star = Picture(vote_top_box, image="images/star.png", height=100, width=100, align="left")
        vote_top_right_star = Picture(vote_top_box, image="images/star.png", height=100, width=100, align="right")

        # box in vote bottom box for stars
        vote_bottom_box_box = Box(vote_bottom_box, width="fill", height=100, align="bottom")

        vote_bottom_left_star = Picture(vote_bottom_box_box, image="images/star.png", height=100, width=100, align="left")
        vote_bottom_right_star = Picture(vote_bottom_box_box, image="images/star.png", height=100, width=100, align="right")

        # vote title and spacer
        vote_title_spacer = Box(vote_top_box, height="fill", width=500, align="left")

        vote_title = Text(vote_top_box, text="VOTE", font="signika", size=90, color="#003566", align="left")

        # boxes in main bottom box
        # 1425/4 = 356.25

        # box for save button
        vote_save_button_box = Box(vote_bottom_box, width="fill", height=80, align="bottom")

        # splitting window into quarters
        vote_q_one = Box(vote_bottom_box, width=356.25, height=535, align="left")
        vote_q_four = Box(vote_bottom_box, width=356.25, height=535, align="right")
        vote_q_two = Box(vote_bottom_box, width=356.25, height=535, align="left")
        vote_q_three = Box(vote_bottom_box, width=356.25, height=535, align="right")

        # boxes in quarters
        vote_q_one_bottom_box = Box(vote_q_one, width="fill", height=250, align="bottom")
        vote_q_two_bottom_box = Box(vote_q_two, width="fill", height=250, align="bottom")
        vote_q_three_bottom_box = Box(vote_q_three, width="fill", height=250, align="bottom")
        vote_q_four_bottom_box = Box(vote_q_four, width="fill", height=250, align="bottom")

        # boxes for name title
        q_one_name_title_box = Box(vote_q_one_bottom_box, width="fill", height=50, align="top")
        q_two_name_title_box = Box(vote_q_two_bottom_box, width="fill", height=50, align="top")
        q_three_name_title_box = Box(vote_q_three_bottom_box, width="fill", height=50, align="top")
        q_four_name_title_box = Box(vote_q_four_bottom_box, width="fill", height=50, align="top")

        # name box
        q_one_name_box = Box(vote_q_one_bottom_box, width="fill", height=50, align="top")
        q_two_name_box = Box(vote_q_two_bottom_box, width="fill", height=50, align="top")
        q_three_name_box = Box(vote_q_three_bottom_box, width="fill", height=50, align="top")
        q_four_name_box = Box(vote_q_four_bottom_box, width="fill", height=50, align="top")

        # spacer between names and candidate number
        q_one_spacer = Box(vote_q_one_bottom_box, width="fill", height=35, align="top")
        q_two_spacer = Box(vote_q_two_bottom_box, width="fill", height=35, align="top")
        q_three_spacer = Box(vote_q_three_bottom_box, width="fill", height=35, align="top")
        q_four_spacer = Box(vote_q_four_bottom_box, width="fill", height=35, align="top")

        # boxes for candidate number
        q_one_candidate_num_title_box = Box(vote_q_one_bottom_box, width="fill", height=50, align="top")
        q_two_candidate_num_title_box = Box(vote_q_two_bottom_box, width="fill", height=50, align="top")
        q_three_candidate_num_title_box = Box(vote_q_three_bottom_box, width="fill", height=50, align="top")
        q_four_candidate_num_title_box = Box(vote_q_four_bottom_box, width="fill", height=50, align="top")

        # candidate number box
        q_one_candidate_num_box = Box(vote_q_one_bottom_box, width="fill", height=50, align="top")
        q_two_candidate_num_box = Box(vote_q_two_bottom_box, width="fill", height=50, align="top")
        q_three_candidate_num_box = Box(vote_q_three_bottom_box, width="fill", height=50, align="top")
        q_four_candidate_num_box = Box(vote_q_four_bottom_box, width="fill", height=50, align="top")

        # spacer in candidate number box
        q_one_candidate_num_spacer = Box(q_one_candidate_num_box, height="fill", width=150, align="left")
        q_two_candidate_num_spacer = Box(q_two_candidate_num_box, height="fill", width=150, align="left")
        q_three_candidate_num_spacer = Box(q_three_candidate_num_box, height="fill", width=150, align="left")
        q_four_candidate_num_spacer = Box(q_four_candidate_num_box, height="fill", width=150, align="left")

        # name titles
        q_one_name_title = Text(q_one_name_title_box, text="name", font="signika", size=70, color="#003566", align="left")
        q_two_name_title = Text(q_two_name_title_box, text="name", font="signika", size=70, color="#003566", align="left")
        q_three_name_title = Text(q_three_name_title_box, text="name", font="signika", size=70, color="#003566", align="left")
        q_four_name_title = Text(q_four_name_title_box, text="name", font="signika", size=70, color="#003566", align="left")

        # candidate number titles
        q_one_candidate_num_title = Text(q_one_candidate_num_title_box, text="candidate no.", font="signika", size=45, color="#003566", align="left")
        q_two_candidate_num_title = Text(q_two_candidate_num_title_box, text="candidate no.", font="signika", size=45, color="#003566", align="left")
        q_three_candidate_num_title = Text(q_three_candidate_num_title_box, text="candidate no.", font="signika", size=45, color="#003566", align="left")
        q_four_candidate_num_title = Text(q_four_candidate_num_title_box, text="candidate no.", font="signika", size=45, color="#003566", align="left")

        # candidate numbers
        q_one_candidate_num = Text(q_one_candidate_num_box, text="1", font="barlow", size=35, color="black", align="left")
        q_two_candidate_num = Text(q_two_candidate_num_box, text="2", font="barlow", size=35, color="black", align="left")
        q_three_candidate_num = Text(q_three_candidate_num_box, text="3", font="barlow", size=35, color="black", align="left")
        q_four_candidate_num = Text(q_four_candidate_num_box, text="4", font="barlow", size=35, color="black", align="left")

        # vote buttons
        q_one_vote = Picture(q_one_candidate_num_box, image="images/vote.png", height=70, width=150, align="right")
        q_one_vote.when_clicked = candidate_one_vote_function

        q_two_vote = Picture(q_two_candidate_num_box, image="images/vote.png", height=70, width=150, align="right")
        q_two_vote.when_clicked = candidate_two_vote_function

        q_three_vote = Picture(q_three_candidate_num_box, image="images/vote.png", height=70, width=150, align="right")
        q_three_vote.when_clicked = candidate_three_vote_function

        q_four_vote = Picture(q_four_candidate_num_box, image="images/vote.png", height=70, width=150, align="right")
        q_four_vote.when_clicked = candidate_four_vote_function

        #  save button for vote window
        vote_save_button = Picture(vote_save_button_box, image="images/save.png", height=80, width=150)
        vote_save_button.when_clicked = vote_save

        # only showing information
        if num_candidates == 2:
            q_three_name_title.text_color = "white"
            q_four_name_title.clear()

            q_three_candidate_num_title.text_color = "white"
            q_four_candidate_num_title.clear()

            q_three_candidate_num.text_color = "white"
            q_four_candidate_num.clear()

            q_three_vote.hide()
            q_four_vote.hide()
        else:
            q_three_name_title.text_color = "#003566"
            q_four_name_title.text_color = "#003566"

            q_three_candidate_num_title.text_color = "#003566"
            q_four_candidate_num_title.text_color = "#003566"

            q_three_candidate_num.text_color = "#003566"
            q_four_candidate_num.text_color = "#003566"

        # if there are only 3 candidates
        if num_candidates == 3:
            q_four_name_title.text_color = "white"

            q_four_candidate_num_title.text_color = "white"

            q_four_candidate_num.text_color = "white"

            q_four_vote.hide()
        else:
            q_four_name_title.text_color = "#003566"

            q_four_candidate_num_title.text_color = "#003566"

            q_four_candidate_num.text_color = "#003566"

        # getting the name of the candidates
        candidate_one_name = candidates[0]
        candidate_two_name = candidates[4]

        # if there are only 2 candidates
        try:
            candidate_three_name = candidates[8]
        except IndexError:
            candidate_three_name = ""

        # if there are only 3 candidates
        try:
            candidate_four_name = candidates[12]
        except IndexError:
            candidate_four_name = ""

        # names of candidates
        q_one_name = Text(q_one_name_box, text=candidate_one_name, font="barlow", size=35, color="black", align="left")
        q_two_name = Text(q_two_name_box, text=candidate_two_name, font="barlow", size=35, color="black", align="left")
        q_three_name = Text(q_three_name_box, text=candidate_three_name, font="barlow", size=35, color="black", align="left")
        q_four_name = Text(q_four_name_box, text=candidate_four_name, font="barlow", size=35, color="black", align="left")

        # going through list
        one_cap_pic = candidates[2]
        two_cap_pic = candidates[6]

        # if there are only 2 candidates
        try:
            three_cap_pic = candidates[10]
        except IndexError:
            three_cap_pic = ""

        # if there are 3 candidates
        try:
            four_cap_pic = candidates[14]
        except IndexError:
            four_cap_pic = ""

        # adding captain pics
        q_one_cap_pic = Picture(vote_q_one, image=one_cap_pic, width=300, height=320)
        q_two_cap_pic = Picture(vote_q_two, image=two_cap_pic, width=300, height=320)

        if three_cap_pic != "":
            q_three_cap_pic = Picture(vote_q_three, image=three_cap_pic, width=300, height=320)

        if four_cap_pic != "":
            q_four_cap_pic = Picture(vote_q_four, image=four_cap_pic, width=300, height=320)

        # showing campaign and poster picture
        q_one_cap_pic.when_mouse_enters = one_info_function
        q_two_cap_pic.when_mouse_enters = two_info_function
        q_three_cap_pic.when_mouse_enters = three_info_function
        q_four_cap_pic.when_mouse_enters = four_info_function

# results window function
def results_window_function():
    global num_candidates, candidates, candidate_one_votes, candidate_two_votes, candidate_three_votes, candidate_four_votes, votes, end_text

    if num_candidates < 2 or votes == 0:
        main.info("info", "there are not enough candidates or votes")
    else:

        results_window = Window(main, title="results", width=1425, height=825)
        results_window.bg = "white"
        results_window.show(wait=True)
        main.hide()

        # back button function
        def results_back_button_function():
            results_window.destroy()
            main.show()

        # top box for results
        results_top_box = Box(results_window, width="fill", height=110)

        # bottom box for results
        results_bottom_box = Box(results_window, width="fill", height=715)

        # box for bottom stars
        bottom_stars_box = Box(results_bottom_box, width="fill", height=100, align="bottom")

        # top stars
        results_top_left_star = Picture(results_top_box, image="images/star.png", width=100, height=100, align="left")
        results_top_right_star = Picture(results_top_box, image="images/star.png", width=100, height=100, align="right")

        # bottom stars
        results_bottom_left_star = Picture(bottom_stars_box, image="images/star.png", width=100, height=100, align="left")
        results_bottom_right_star = Picture(bottom_stars_box, image="images/star.png", width=100, height=100, align="right")

        # spacer between star and title
        results_top_box_spacer = Box(results_top_box, height="fill", width=437, align="left")

        # results title
        results_title = Text(results_top_box, text="RESULTS", font="signika", size=90, color="#003566", align="left")

        # box for winner title
        text_title_box = Box(results_bottom_box, width="fill", height=125, align="top")

        # box for back button
        results_back_button_box = Box(results_bottom_box, width="fill", height=70, align="bottom")

        # splitting bottom quarters
        results_q_one = Box(results_bottom_box, width=356.25, height="fill", align="left")
        results_q_four = Box(results_bottom_box, width=356.25, height="fill", align="right")
        results_q_two = Box(results_bottom_box, width=356.25, height="fill", align="left")
        results_q_three = Box(results_bottom_box, width=356.25, height="fill", align="right")

        # finding the candidate with the most votes
        # comparing one and two
        if num_candidates == 2:
            if candidate_one_votes > candidate_two_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_one.bg = "#ffd60a"
            elif candidate_two_votes > candidate_one_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_two.bg = "#ffd60a"
            else:
                end_text = "NO CLEAR WINNER"

        # comparing 1, 2 and 3
        if num_candidates == 3:
            if candidate_one_votes > candidate_two_votes and candidate_one_votes > candidate_three_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_one.bg = "#ffd60a"
            elif candidate_two_votes > candidate_three_votes and candidate_two_votes > candidate_one_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_two.bg = "#ffd60a"
            elif candidate_three_votes > candidate_one_votes and candidate_three_votes > candidate_two_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_three.bg = "#ffd60a"
            else:
                end_text = "NO CLEAR WINNER"

        # comparing 1, 2, 3 and 4
        if num_candidates == 4:
            if candidate_one_votes > candidate_two_votes and candidate_one_votes > candidate_three_votes and candidate_one_votes > candidate_four_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_one.bg = "#ffd60a"
            elif candidate_two_votes > candidate_three_votes and candidate_two_votes > candidate_four_votes and candidate_two_votes > candidate_one_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_two.bg = "#ffd60a"
            elif candidate_three_votes > candidate_four_votes and candidate_three_votes > candidate_one_votes and candidate_three_votes > candidate_two_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_three.bg = "#ffd60a"
            elif candidate_four_votes > candidate_one_votes and candidate_four_votes > candidate_two_votes and candidate_four_votes > candidate_three_votes:
                end_text = "NEW CLASS CAPTAIN"
                results_q_four.bg = "#ffd60a"
            else:
                end_text = "NO CLEAR WINNER"

        text_title = Text(text_title_box, text=end_text, font="signika", size=100, color="#003566")

        # boxes for names and candidates
        results_q_one_box = Box(results_q_one, width=356.25, height=170, align="bottom")
        results_q_two_box = Box(results_q_two, width=356.25, height=170, align="bottom")
        results_q_three_box = Box(results_q_three, width=356.25, height=170, align="bottom")
        results_q_four_box = Box(results_q_four, width=356.25, height=170, align="bottom")

        # boxes for name title
        q_one_name_title_box = Box(results_q_one_box, width="fill", height=40, align="top")
        q_two_name_title_box = Box(results_q_two_box, width="fill", height=40, align="top")
        q_three_name_title_box = Box(results_q_three_box, width="fill", height=40, align="top")
        q_four_name_title_box = Box(results_q_four_box, width="fill", height=40, align="top")

        # boxes for name
        q_one_name_box = Box(results_q_one_box, width="fill", height=40, align="top")
        q_two_name_box = Box(results_q_two_box, width="fill", height=40, align="top")
        q_three_name_box = Box(results_q_three_box, width="fill", height=40, align="top")
        q_four_name_box = Box(results_q_four_box, width="fill", height=40, align="top")

        # spacer
        q_one_spacer = Box(results_q_one_box, width="fill", height=15, align="top")
        q_two_spacer = Box(results_q_two_box, width="fill", height=15, align="top")
        q_three_spacer = Box(results_q_three_box, width="fill", height=15, align="top")
        q_four_spacer = Box(results_q_four_box, width="fill", height=15, align="top")

        # boxes for candidate number title
        q_one_candidate_num_title_box = Box(results_q_one_box, width="fill", height=40, align="top")
        q_two_candidate_num_title_box = Box(results_q_two_box, width="fill", height=40, align="top")
        q_three_candidate_num_title_box = Box(results_q_three_box, width="fill", height=40, align="top")
        q_four_candidate_num_title_box = Box(results_q_four_box, width="fill", height=40, align="top")

        # boxes for candidate number
        q_one_candidate_num_box = Box(results_q_one_box, width="fill", height=35, align="top")
        q_two_candidate_num_box = Box(results_q_two_box, width="fill", height=35, align="top")
        q_three_candidate_num_box = Box(results_q_three_box, width="fill", height=35, align="top")
        q_four_candidate_num_box = Box(results_q_four_box, width="fill", height=35, align="top")

        # name titles
        q_one_name_title = Text(q_one_name_title_box, text="name", font="signika", size=50, color="#003566", align="left")
        q_two_name_title = Text(q_two_name_title_box, text="name", font="signika", size=50, color="#003566", align="left")
        q_three_name_title = Text(q_three_name_title_box, text="name", font="signika", size=50, color="#003566", align="left")
        q_four_name_title = Text(q_four_name_title_box, text="name", font="signika", size=50, color="#003566", align="left")

        # candidate titles
        q_one_candidate_num_title = Text(q_one_candidate_num_title_box, text="candidate no.", font="signika", size=35, color="#003566", align="left")
        q_two_candidate_num_title = Text(q_two_candidate_num_title_box, text="candidate no.", font="signika", size=35, color="#003566", align="left")
        q_three_candidate_num_title = Text(q_three_candidate_num_title_box, text="candidate no.", font="signika", size=35, color="#003566", align="left")
        q_four_candidate_num_title = Text(q_four_candidate_num_title_box, text="candidate no.", font="signika", size=35, color="#003566", align="left")

        # candidate numbers
        q_one_candidate_num = Text(q_one_candidate_num_box, text="1", font="barlow", size=30, color="black")
        q_two_candidate_num = Text(q_two_candidate_num_box, text="2", font="barlow", size=30, color="black")
        q_three_candidate_num = Text(q_three_candidate_num_box, text="3", font="barlow", size=30, color="black")
        q_four_candidate_num = Text(q_four_candidate_num_box, text="4", font="barlow", size=30, color="black")

        # getting the name of the candidates
        candidate_one_name = candidates[0]
        candidate_two_name = candidates[4]

        # if there are only 2 candidates
        try:
            candidate_three_name = candidates[8]
        except IndexError:
            candidate_three_name = ""

        # if there are only 3 candidates
        try:
            candidate_four_name = candidates[12]
        except IndexError:
            candidate_four_name = ""

        # names of candidates
        q_one_name = Text(q_one_name_box, text=candidate_one_name, font="barlow", size=35, color="black", align="left")
        q_two_name = Text(q_two_name_box, text=candidate_two_name, font="barlow", size=35, color="black", align="left")
        q_three_name = Text(q_three_name_box, text=candidate_three_name, font="barlow", size=35, color="black", align="left")
        q_four_name = Text(q_four_name_box, text=candidate_four_name, font="barlow", size=35, color="black", align="left")

        # only showing information where there is information to be displayed. e.g. if there are only 2 candidates, name gets shown twice
        if num_candidates == 2:
            q_three_name_title.text_color = "white"
            q_four_name_title.clear()

            q_three_candidate_num_title.text_color = "white"
            q_four_candidate_num_title.clear()

            q_three_candidate_num.text_color = "white"
            q_four_candidate_num.clear()

        else:
            q_three_name_title.text_color = "#003566"
            q_four_name_title.text_color = "#003566"

            q_three_candidate_num_title.text_color = "#003566"
            q_four_candidate_num_title.text_color = "#003566"

            q_three_candidate_num.text_color = "#003566"
            q_four_candidate_num.text_color = "#003566"

        # if there are 3 candidates
        if num_candidates == 3:
            q_four_name_title.text_color = "white"

            q_four_candidate_num_title.text_color = "white"

            q_four_candidate_num.text_color = "white"

        else:
            q_four_name_title.text_color = "#003566"

            q_four_candidate_num_title.text_color = "#003566"

            q_four_candidate_num.text_color = "#003566"

        # showing captain pic
        one_cap_pic = candidates[2]
        two_cap_pic = candidates[6]

        try:
            three_cap_pic = candidates[10]
        except IndexError:
            three_cap_pic = ""

        try:
            four_cap_pic = candidates[14]
        except IndexError:
            four_cap_pic = ""

        one_pic = Picture(results_q_one, image=one_cap_pic, height=300, width=350)
        two_pic = Picture(results_q_two, image=two_cap_pic, height=300, width=350)

        if three_cap_pic != "":
            three_cap_pic = Picture(results_q_three, image=three_cap_pic, height=300, width=350)

        if four_cap_pic != "":
            four_cap_pic = Picture(results_q_four, image=four_cap_pic, height=300, width=350)

        # back button
        results_back_button = Picture(results_back_button_box, image="images/back.png", width=150, height=70)
        results_back_button.when_clicked = results_back_button_function

# statistics window function
def stats_window_function():
    global votes, num_candidates, adding_captain_picture, adding_campaign_poster, candidate_one_votes, candidate_two_votes, candidate_three_votes, candidate_four_votes
    if num_candidates < 2 or votes == 0:
        main.info("info", "there are not enough candidates or votes")
    else:
        stats_window = Window(main, title="statistics", width=1425, height=825)
        stats_window.bg = "white"
        stats_window.show(wait=True)
        main.hide()

        # back button function
        def stats_back_button_function():
            stats_window.destroy()
            main.show()

        # top box
        stats_top_box = Box(stats_window, width="fill", height=110, align="top")

        # bottom box
        stats_bottom_box = Box(stats_window, width="fill", height=715, align="bottom")

        # stats top stars
        stats_top_left_star = Picture(stats_top_box, image="images/star.png", width=100, height=100, align="left")
        stats_top_right_star = Picture(stats_top_box, image="images/star.png", width=100, height=100, align="right")

        # stats bottom stars box
        stats_bottom_stars_box = Box(stats_bottom_box, width="fill", height=100, align="bottom")

        # stats bottom stars
        stats_bottom_left_star = Picture(stats_bottom_stars_box, image="images/star.png", width=100, height=100, align="left")
        stats_bottom_right_star = Picture(stats_bottom_stars_box, image="images/star.png", width=100, height=100, align="right")

        # back button box
        stats_back_button_box = Box(stats_bottom_box, width="fill", height=70, align="bottom")

        # spacer between star and title
        stats_top_spacer = Box(stats_top_box, height="fill", width=390, align="left")

        # stats title
        stats_title = Text(stats_top_box, text="STATISTICS", font="signika", size=90, color="#003566", align="left")

        # splitting into quarters
        stats_q_one = Box(stats_bottom_box, width=356.25, height="fill", align="left")
        stats_q_four = Box(stats_bottom_box, width=356.25, height="fill", align="right")
        stats_q_two = Box(stats_bottom_box, width=356.25, height="fill", align="left")
        stats_q_three = Box(stats_bottom_box, width=356.25, height="fill", align="right")

        # boxes for names and candidates
        stats_q_one_box = Box(stats_q_one, width=356.25, height=170, align="bottom")
        stats_q_two_box = Box(stats_q_two, width=356.25, height=170, align="bottom")
        stats_q_three_box = Box(stats_q_three, width=356.25, height=170, align="bottom")
        stats_q_four_box = Box(stats_q_four, width=356.25, height=170, align="bottom")

        # name boxes
        q_one_name_title_box = Box(stats_q_one_box, width="fill", height=50, align="top")
        q_two_name_title_box = Box(stats_q_two_box, width="fill", height=50, align="top")
        q_three_name_title_box = Box(stats_q_three_box, width="fill", height=50, align="top")
        q_four_name_title_box = Box(stats_q_four_box, width="fill", height=50, align="top")

        # name title box
        q_one_name_box = Box(q_one_name_title_box, height=50, width=100, align="left")
        q_two_name_box = Box(q_two_name_title_box, height=50, width=100, align="left")
        q_three_name_box = Box(q_three_name_title_box, height=50, width=100, align="left")
        q_four_name_box = Box(q_four_name_title_box, height=50, width=100, align="left")

        # name title
        q_one_name_title = Text(q_one_name_box, text="name: ", font="signika", size=40, color="#003566")
        q_two_name_title = Text(q_two_name_box, text="name: ", font="signika", size=40, color="#003566")
        q_three_name_title = Text(q_three_name_box, text="name: ", font="signika", size=40, color="#003566")
        q_four_name_title = Text(q_four_name_box, text="name: ", font="signika", size=40, color="#003566")

        # spacers
        one_spacer = Box(stats_q_one_box, height=10, width="fill", align="top")
        two_spacer = Box(stats_q_two_box, height=10, width="fill", align="top")
        three_spacer = Box(stats_q_three_box, height=10, width="fill", align="top")
        four_spacer = Box(stats_q_four_box, height=10, width="fill", align="top")

        # candidate num title box
        q_one_c_title_box = Box(stats_q_one_box, height=50, width="fill", align="top")
        q_two_c_title_box = Box(stats_q_two_box, height=50, width="fill", align="top")
        q_three_c_title_box = Box(stats_q_three_box, height=50, width="fill", align="top")
        q_four_c_title_box = Box(stats_q_four_box, height=50, width="fill", align="top")

        # candidate title box
        q_one_c_title = Box(q_one_c_title_box, height=50, width=300, align="left")
        q_two_c_title = Box(q_two_c_title_box, height=50, width=300, align="left")
        q_three_c_title = Box(q_three_c_title_box, height=50, width=300, align="left")
        q_four_c_title = Box(q_four_c_title_box, height=50, width=300, align="left")

        # candidate title
        q_one_c = Text(q_one_c_title, text="candidate no.", font="signika", size=40, color="#003566")
        q_two_c = Text(q_two_c_title, text="candidate no.", font="signika", size=40, color="#003566")
        q_three_c = Text(q_three_c_title, text="candidate no.", font="signika", size=40, color="#003566")
        q_four_c = Text(q_four_c_title, text="candidate no.", font="signika", size=40, color="#003566")

        # candidate num
        q_one_c_num = Text(q_one_c_title_box, text="1", font="barlow", size=40, color="black")
        q_two_c_num = Text(q_two_c_title_box, text="2", font="barlow", size=40, color="black")
        q_three_c_num = Text(q_three_c_title_box, text="3", font="barlow", size=40, color="black")
        q_four_c_num = Text(q_four_c_title_box, text="4", font="barlow", size=40, color="black")

        # spacer pt. 2
        one_spacer_2 = Box(stats_q_one_box, height=10, width="fill", align="top")
        two_spacer_2 = Box(stats_q_two_box, height=10, width="fill", align="top")
        three_spacer_2 = Box(stats_q_three_box, height=10, width="fill", align="top")
        four_spacer_2 = Box(stats_q_four_box, height=10, width="fill", align="top")

        # votes box
        q_one_vote_box = Box(stats_q_one_box, height=50, width="fill", align="top")
        q_two_vote_box = Box(stats_q_two_box, height=50, width="fill", align="top")
        q_three_vote_box = Box(stats_q_three_box, height=50, width="fill", align="top")
        q_four_vote_box = Box(stats_q_four_box, height=50, width="fill", align="top")

        # vote title box
        q_one_vote_title_box = Box(q_one_vote_box, width=200, height="fill", align="left")
        q_two_vote_title_box = Box(q_two_vote_box, width=200, height="fill", align="left")
        q_three_vote_title_box = Box(q_three_vote_box, width=200, height="fill", align="left")
        q_four_vote_title_box = Box(q_four_vote_box, width=200, height="fill", align="left")

        # vote title
        q_one_vote_title = Text(q_one_vote_title_box, text="vote(s)", font="signika", size=40, color="#003566")
        q_two_vote_title = Text(q_two_vote_title_box, text="vote(s)", font="signika", size=40, color="#003566")
        q_three_vote_title = Text(q_three_vote_title_box, text="vote(s)", font="signika", size=40, color="#003566")
        q_four_vote_title = Text(q_four_vote_title_box, text="vote(s)", font="signika", size=40, color="#003566")

        # votes out of 30
        q_one_votes = str(candidate_one_votes) + "/" + str(votes)
        q_two_votes = str(candidate_two_votes) + "/" + str(votes)
        q_three_votes = str(candidate_three_votes) + "/" + str(votes)
        q_four_votes = str(candidate_four_votes) + "/" + str(votes)

        # votes
        q_one_v = Text(q_one_vote_box, text=q_one_votes, font="barlow", size=40, color="black")
        q_two_v = Text(q_two_vote_box, text=q_two_votes, font="barlow", size=40, color="black")
        q_three_v = Text(q_three_vote_box, text=q_three_votes, font="barlow", size=40, color="black")
        q_four_v = Text(q_four_vote_box, text=q_four_votes, font="barlow", size=40, color="black")

        # getting the name of the candidates
        candidate_one_name = candidates[0]
        candidate_two_name = candidates[4]

        # if there are only 2 candidates
        try:
            candidate_three_name = candidates[8]
        except IndexError:
            candidate_three_name = ""

        # if there are only 3 candidates
        try:
            candidate_four_name = candidates[12]
        except IndexError:
            candidate_four_name = ""

        # names of candidates
        q_one_name = Text(q_one_name_title_box, text=candidate_one_name, font="barlow", size=35, color="black", align="left")
        q_two_name = Text(q_two_name_title_box, text=candidate_two_name, font="barlow", size=35, color="black", align="left")
        q_three_name = Text(q_three_name_title_box, text=candidate_three_name, font="barlow", size=35, color="black", align="left")
        q_four_name = Text(q_four_name_title_box, text=candidate_four_name, font="barlow", size=35, color="black", align="left")

        if num_candidates == 2:
            q_three_name_title.text_color = "white"
            q_three_name.text_color = "white"

            q_three_c_title.text_color = "white"
            q_three_c_num.text_color = "white"

            q_three_vote_title.text_color = "white"
            q_three_v.text_color = "white"


            q_four_name_title.text_color = "white"
            q_four_name.text_color = "white"

            q_four_c_title.text_color = "white"
            q_four_c_num.text_color = "white"

            q_four_vote_title.text_color = "white"
            q_four_v.text_color = "white"

        if num_candidates == 3:
            q_four_name_title.text_color = "white"
            q_four_name.text_color = "white"

            q_four_c_title.text_color = "white"
            q_four_c_num.text_color = "white"

            q_four_vote_title.text_color = "white"
            q_four_v.text_color = "white"

        # showing captain pic
        one_cap_pic = candidates[2]
        two_cap_pic = candidates[6]

        try:
            three_cap_pic = candidates[10]
        except IndexError:
            three_cap_pic = ""

        try:
            four_cap_pic = candidates[14]
        except IndexError:
            four_cap_pic = ""

        one_pic = Picture(stats_q_one, image=one_cap_pic, height=300, width=350)
        two_pic = Picture(stats_q_two, image=two_cap_pic, height=300, width=350)

        if three_cap_pic != "":
            three_cap_pic = Picture(stats_q_three, image=three_cap_pic, height=300, width=350)

        if four_cap_pic != "":
            four_cap_pic = Picture(stats_q_four, image=four_cap_pic, height=300, width=350)

        # back button
        stats_back_button = Picture(stats_back_button_box, image="images/back.png", width=150, height=70)
        stats_back_button.when_clicked = stats_back_button_function

# main window
main = App(title="class captain", width=1425, height=825)
# 1425 divided by 3 = 475
main.bg = "white"

# main top box
main_top_box = Box(main, width="fill", height=110, border=False, align="top")

# main bottom box
main_bottom_box = Box(main, width="fill", height=715, border=False, align="bottom")

# box for bottom stars in main
main_bottom_box_box = Box(main_bottom_box, width="fill", height=100, border=False, align="bottom")

# stars for top in main
main_top_left_star = Picture(main_top_box, image="images/star.png", width=100, height=100, align="left")
main_top_right_star = Picture(main_top_box, image="images/star.png", width=100, height=100, align="right")

# stars in bottom in main
main_bottom_left_star = Picture(main_bottom_box_box, image="images/star.png", width=100, height=100, align="left")
main_bottom_right_star = Picture(main_bottom_box_box, image="images/star.png", width=100, height=100, align="right")

# spacer in top box
main_top_spacer = Box(main_top_box, height="fill", width=490, align="left", border=False)

# main menu title
main_title = Text(main_top_box, text="MENU", font="signika", size=90, color="#003566", align="left")

# boxes in bottom box in main
main_bottom_box_left_box = Box(main_bottom_box, height="fill", width=510, align="left", border=False)
main_bottom_box_right_box = Box(main_bottom_box, height="fill", width=510, align="right", border=False)
main_bottom_box_middle_box = Box(main_bottom_box, height="fill", width=405, border=False)

# box in main left bottom box
main_bottom_box_left_box_box = Box(main_bottom_box_left_box, height=300, width="fill", align="top", border=False)

# top spacer in main left bottom box
main_bottom_box_left_spacer_top = Box(main_bottom_box_left_box_box, height=50, width="fill", align="top", border=False)

# bottom spacer in main left bottom box
main_bottom_box_left_spacer_bottom = Box(main_bottom_box_left_box, height=50, width="fill", align="bottom", border=False)

# box in main right bottom box
main_bottom_box_right_box_box = Box(main_bottom_box_right_box, height=300, width="fill", align="top", border=False)

# top spacer in main right bottom box
main_bottom_box_right_spacer_top = Box(main_bottom_box_right_box_box, height=50, width="fill", align="top", border=False)

# bottom spacer in main right bottom box
main_bottom_box_right_spacer_bottom = Box(main_bottom_box_right_box, height=50, width="fill", align="bottom", border=False)

# star image in center
# spacer for image
main_middle_star_spacer = Box(main_bottom_box_middle_box, width="fill", height=100, align="top", border=False)
main_middle_star = Picture(main_bottom_box_middle_box, image="images/star.png", height=400, width=400, align="top")

# BUTTONS

# add profile button
add_profile = Picture(main_bottom_box_left_box_box, image="images/add profile.png", width=275, height=148, align="right")

# when user clicks on image
add_profile.when_clicked = add_profile_window_function

# vote button
vote = Picture(main_bottom_box_left_box, image="images/vote.png", width=275, height=148, align="right")
vote.when_clicked = vote_window_function

# results button
results = Picture(main_bottom_box_right_box_box, image="images/results.png", width=275, height=148, align="left")

# when user clicks on image
results.when_clicked = results_window_function

# statistics button
statistics = Picture(main_bottom_box_right_box, image="images/statistics.png", width=275, height=148, align="left")

# when user clicks on image
statistics.when_clicked = stats_window_function

main.display()
