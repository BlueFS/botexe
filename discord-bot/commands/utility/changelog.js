const { SlashCommandBuilder} = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('Changelog')
        .setDescription('What has changes have been made'),
    async execute(interaction) {
        await interaction.reply('There is none right now. Bot Version: v1.1');
    },
};
//Please change the changelog before pushing a new update
