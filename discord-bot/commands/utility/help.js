const { SlashCommandBuilder} = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('help')
        .setDescription('Support'),
    async execute(interaction) {
        await interaction.reply('Contact BlueFS or SlipperyBooney on Discord');
    },
};
