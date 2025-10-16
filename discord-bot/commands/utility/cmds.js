const { SlashCommandBuilder } = require('discord.js')
const { EmbedBuilder } = require('discord.js')

module.exports = {
    data: new SlashCommandBuilder()
        .setName('cmds')
        .setDescription('Shows the lists of commands'),
    async execute(interaction) {
        const embed = new EmbedBuilder()
            .setTitle('Command List')
            .setColor(0x5865F2)
            .addFields(
                {name: '/cmds', value: 'Displays all  the commands.', inline: false},
                {name: '/ping', value: 'Replies with pong.', inline: false},
                {name: '/bug', value: 'NOT YET IMPLEMENTED -- Allows user to submit a bug report.', inline: false},
                {name: '/dev', value: 'Idk.', inline: false},

            );
        await interaction.reply({ embeds: [embed]});
    },
};