const { SlashCommandBuilder} = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
        .setname('dev')
        .setdescription('Who to contact for help?'),
  async execue(interaction) {
    await interation.reply('Please Contact @Blue and or @SlipperyBooney :P);
                           },
};
