const { SlashCommandBuilder} = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('dev')
        .setDescription('Totally the dev button!'),
    async execute(interaction) {
        await interaction.reply('This is a dev button :P');
    },
};