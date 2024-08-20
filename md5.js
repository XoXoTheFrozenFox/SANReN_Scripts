const CryptoJS = require('crypto-js');

// MD5 hash to compare
const targetHash = '531e769c0d92a3a1e395f88f839dffa3';

// List of words to test
const words = [
    "cotton_factory_offline_",
    "nerve_of_steel_",
    "bay_of_hounds_",
    "disorder_leads_to_chaos_",
    "dream_sweet_my_love_",
    "plan_B_",
    "trail_Went_cold_",
    "article_for_your_attention_",
    "royalty_usally_stick_",
    "chimpanzee_will_take_over_",
    "language_as_we_know_it_is_dead_",
    "advertising_make_money_",
    "dangerous_skills_dangerous_work_",
    "cut_and_past_",
    "feign_parry_repose_strike_",
    "bread_for_bed_",
    "protest_vs_teargass_",
    "banks_started_capitalism_",
    "buttocks_for_for_the_win_",
    "ferry_can_sink_",
    "mercy_is_for_the_Weak_",
    "abuse_is_real_",
    "decisive_action_leads_to_change_",
    "ditch_is_where_we_all_end_up_",
    "ritual_for_cookies_",
    "MD5_is_not_secure_",
    "diplomatic_above_war_",
    "ear_worm_brain_dead_",
    "government_lies_allways_",
    "cage_only_you_can_break_",
    "toll_the_bell_",
    "introduce_Thoughts_take_your_meds_",
    "live_with_the_one_and_only_",
    "horse_riding_on_the_beach_",
    "volume_up_or_down_",
    "dirty_minds_leads_to_violent_delights_",
    "quest_reward_insufficiant_",
    "air_in_and_air_out_",
    "lighter_darker_clearer_",
    "jungle_book_best_",
    "palace_in_the_east_",
    "appointment_at_seven_",
    "establish_a_collony_at_roanoke_",
    "outlet_inlet_",
    "adult_only_",
    "excavation_of_the_mind_",
    "transaction_complete_",
    "duck_duck_go_",
    "deter_von_eckhard_the_third_"
];

// Function to calculate MD5 hash of a given string
function md5Hash(text) {
    return CryptoJS.MD5(text).toString();
}

// Check each word
for (const word of words) {
    if (md5Hash(word) === targetHash) {
        console.log(`Match found: ${word}`);
        break;
    }
    else{
        console.log("No match found.");
    }
}
